from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.template.loader import get_template
from django.utils.translation import gettext as _
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, \
    NestedStackedInline

from .forms import *
from .models import *


class ImageAdmin(admin.ModelAdmin):
    model = Image


class RentalRealtyInline(NestedTabularInline, GenericTabularInline):
    model = RentalRealty
    extra = 0


class SaleRealtyInline(NestedTabularInline, GenericTabularInline):
    model = SaleRealty
    extra = 0


class ImageInline(NestedTabularInline, GenericTabularInline):
    model = Image
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("show_thumbnail.html")
        return tpl.render({"photo": instance.photo})
    showphoto_thumbnail.short_description = _("Thumbnail")


# class RoomAdmin(admin.ModelAdmin):
#     model = Room
#     search_fields = ('home__home__street', 'home__home__home', 'home__flat')


class RoomInline(NestedTabularInline, GenericTabularInline):
    model = Room
    extra = 1
    inlines = [RentalRealtyInline, SaleRealtyInline]


class DetachedHouseAdmin(admin.ModelAdmin):
    form = DetachedHouseAdminForm
    inlines = [RentalRealtyInline, SaleRealtyInline, RoomInline, ImageInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


class FlatInline(NestedStackedInline):
    model = Flat
    form = FlatAdminForm
    extra = 1
    inlines = [RentalRealtyInline, SaleRealtyInline, RoomInline, ImageInline]


class ApartmentAdmin(NestedModelAdmin):
    model = Apartment
    inlines = [FlatInline]
    search_fields = ('street', 'home')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('apartment__street', 'apartment__home')
    form = FlatAdminForm
    model = Flat
    inlines = [ImageInline, RoomInline, RentalRealtyInline, SaleRealtyInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


class LandPlotAdmin(admin.ModelAdmin):
    search_fields = ('street', 'land_area')
    form = LandPlotAdminForm
    inlines = [ImageInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


admin.site.register(TechnicChoices)
admin.site.register(DetachedHouse, DetachedHouseAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(LandPlot, LandPlotAdmin)
admin.site.register(FurnitureChoice)
admin.site.register(Apartment, ApartmentAdmin)
# admin.site.register(Room, RoomAdmin)
admin.site.register(Image, ImageAdmin)
