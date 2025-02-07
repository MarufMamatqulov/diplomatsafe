from rest_framework import serializers
from .models import Safe, Category, Model, ModelImage, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImage
        fields = ('image', 'order')


class ModelSerializer(serializers.ModelSerializer):
    images = ModelImageSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Model
        fields = ('id', 'name', 'brand', 'images', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SafeSerializer(serializers.ModelSerializer):
    model = ModelSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Safe
        fields = (
            'id', 'name', 'description', 'price', 'dimensions', 'weight',
            'material', 'lock_type', 'fire_resistance', 'warranty',
            'is_available', 'features', 'quantity', 'category', 'model', 'slug'
        )