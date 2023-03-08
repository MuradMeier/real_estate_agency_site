from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from multiselectfield import MultiSelectField

BATHROOM_LOCATION = (
    ("In street", "На улице"),
    ("In house", "В доме"),
)

COMMUNICATIONS = (
    ("Water", "Вода"),
    ("Light", "Свет"),
    ("Gas", "Газ"),
)

BATHROOM_TYPES = (
    ("Separate", "Раздельный"),
    ("Adjective", "Смежный"),
)

WATER_SUPPLY = (
    ("Pit", "Колодец"),
    ("Borehole", "Скважина"),
    ("Сentral", "Центральное"),
)
BALCONY_OR_LOGGIA = (
    ("Balcony", "Балкон"),
    ("Loggia", "Лоджия"),
)
LAND_TYPE = (
    ("ИЖС", "ИЖС"),
    ("СНТ", "СНТ"),
)
SEVERAGE_TYPE = (
    ("Central", "Центральная"),
    ("Local", "Локальная")
)


class Image(models.Model):
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos/')
    realty = GenericForeignKey("content_type", "object_id")


class Realty(models.Model):

    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255, verbose_name='Улица')
    images = GenericRelation(Image)

    def __str__(self):
        return self.street


class LandPlot(Realty):

    class Meta:
        verbose_name = 'Земельный участок'
        verbose_name_plural = 'Земельные участки'

    land_area = models.PositiveIntegerField(verbose_name='Площадь участка')
    is_water = models.BooleanField(verbose_name="Вода")
    is_severage = models.BooleanField(verbose_name="Канализация")
    is_gas = models.BooleanField(verbose_name="Газ")
    land_type = models.CharField(choices=LAND_TYPE, verbose_name="Участок",
                                 max_length=3)

    def __str__(self):
        return self.street


class TechnicChoices(models.Model):
    class Meta:
        verbose_name_plural = "Техника"
    choice = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.choice


class FurnitureChoice(models.Model):
    class Meta:
        verbose_name_plural = "Мебель"
    choice = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.choice


class ResidentialRealty(Realty):
    class Meta:
        abstract = True

    year_construction = models.PositiveIntegerField(
        verbose_name='Год постройки')
    home = models.PositiveIntegerField(verbose_name='Дом')

    class RealtyType(models.TextChoices):
        brick = ("Кирпич", "Кирпич")
        monolith = ("Монолит", "Монолит")
        panel = ("Панельный", "Панельный")

    realty_type = models.CharField(choices=RealtyType.choices, max_length=255,
                                   verbose_name='Тип дома',
                                   default=RealtyType.monolith)
    floor_in_house = models.PositiveIntegerField(
        verbose_name='Количество этажей')


class Apartment(ResidentialRealty):
    class Meta:
        verbose_name = 'Многоэтажка'
        verbose_name_plural = "Многоэтажки"
    elevator = models.BooleanField(verbose_name='Лифт')

    def __str__(self):
        return f"{self.street} {self.home}"


class DetachedHouse(ResidentialRealty):
    class Meta:
        verbose_name = 'Частный дом'
        verbose_name_plural = "Частные дома"
    bathroom_location = MultiSelectField(
        verbose_name='Местоположение санузлов', choices=BATHROOM_LOCATION,
        max_length=9, blank=True)

    distance_to_city_center = models.PositiveIntegerField(
        verbose_name='Расстояние до центра, км')
    communications = MultiSelectField(verbose_name='Коммуникации',
                                      choices=COMMUNICATIONS, max_length=5,
                                      blank=True)
    land_area = models.PositiveIntegerField(verbose_name='Площадь участка')
    home_area = models.PositiveIntegerField(verbose_name='Жил площадь')

    water_type = MultiSelectField(verbose_name="Источник воды",
                                  choices=WATER_SUPPLY, max_length=9,
                                  blank=True)
    severage_type = MultiSelectField(verbose_name="Тип канализации",
                                     max_length=12, choices=SEVERAGE_TYPE,
                                     blank=True)
    room = GenericRelation('Room')
    quantity_rooms = models.PositiveIntegerField(
        verbose_name='Количество комнат')

    def __str__(self):
        return f"{self.street} {self.home}"


class Room(models.Model):
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = "Комнаты"
    room_area = models.PositiveIntegerField(verbose_name='Площадь комнаты',
                                            blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.PositiveIntegerField()
    home = GenericForeignKey("content_type", "object_id")


class BalconyOrLoggiaChoices(models.Model):
    choice = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.choice


class Flat(models.Model):
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = "Квартиры"

    class RoomsType(models.TextChoices):
        adjective = ("Смежный", "Смежный")
        separate = ("Раздельный", "Раздельный")

    class Renovation(models.TextChoices):
        euro = ("Евро", "Евро")
        cosmetic = ("Косметический", "Косметический")
        capital = ("Капитальный", "Капитальный")
        designer = ("Дизайнерский", "Дизайнерский")

    bathroom_quantity = models.IntegerField(verbose_name='Число санузлов',
                                            default=1)
    bathroom_type = MultiSelectField(verbose_name='Типы санузлов',
                                     choices=BATHROOM_TYPES, max_length=10)
    floor = models.IntegerField(verbose_name='Этаж')
    is_balcony_or_loggia = MultiSelectField(verbose_name='Балкон / лоджия',
                                            choices=BALCONY_OR_LOGGIA,
                                            max_length=7, blank=True)
    rooms_type = models.CharField(max_length=255, verbose_name='Тип комнат',
                                  choices=RoomsType.choices)
    technic = models.ManyToManyField(TechnicChoices, verbose_name='Техника',
                                     blank=True)
    furniture = models.ManyToManyField(FurnitureChoice, max_length=512,
                                       verbose_name='Мебель', blank=True)
    renovation = models.CharField(choices=Renovation.choices, max_length=255,
                                  verbose_name='Ремонт', blank=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    home_area = models.PositiveIntegerField(verbose_name='Жил площадь')
    flat = models.PositiveIntegerField(verbose_name='Квартира')
    quantity_rooms = models.PositiveIntegerField(
        verbose_name='Количество комнат')

    def __str__(self):
        return f'{self.quantity_rooms}-x к. кв. , {self.home_area} кв.м.'


class RentalRealty(models.Model):
    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренда'
    smoke = models.BooleanField(verbose_name='Можно курить')
    child = models.BooleanField(verbose_name='Можно с детьми')
    animal = models.BooleanField(verbose_name='Можно с животными')
    sleeping_place = models.IntegerField(
        verbose_name='Количество спальных мест', default=1)
    price = models.IntegerField(verbose_name='Цена')
    content_type = models.OneToOneField(ContentType, on_delete=models.RESTRICT)
    object_id = models.PositiveIntegerField()
    realty = GenericForeignKey("content_type", "object_id")


class SaleRealty(models.Model):
    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажа'
    price = models.IntegerField(verbose_name='Цена')
    content_type = models.OneToOneField(ContentType, on_delete=models.RESTRICT)
    object_id = models.PositiveIntegerField()
    realty = GenericForeignKey("content_type", "object_id")
