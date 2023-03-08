from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = '__all__'


class LandPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandPlot
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apartment
        fields = '__all__'


class FlatSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer()
    images = ImageSerializer(source='image_set', many=True, read_only=True)

    class Meta:
        model = Flat
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        flat = Flat.objects.create(
            bathroom_quantity=validated_data.get('bathroom_quantity'),
            bathroom_type=validated_data.get('bathroom_type'),
            floor=validated_data.get('floor'),
            is_balcony_or_loggia=validated_data.get('is_balcony_or_loggia'),
            rooms_type=validated_data.get('rooms_type'),
            technic=validated_data.get('technic'),
            furniture=validated_data.get('furniture'),
            renovation=validated_data.get('renovation'),
            apartment=validated_data.get('apartment'),
            home_area=validated_data.get('home_area'),
            flat=validated_data.get('flat'),
            quantity_rooms=validated_data.get('quantity_rooms'),
        )
        for image_data in images_data.values():
            Image.objects.create(flat=flat, image=image_data)
        return flat


class RoomSerializer(serializers.ModelSerializer):
    home = FlatSerializer()

    class Meta:
        model = Room
        fields = '__all__'

