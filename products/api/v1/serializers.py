from rest_framework.fields import SerializerMethodField

from products.models import Category, Subcategory, Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    subcategory = SerializerMethodField()
    images = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'name', 'slug', 'price', 'images']
        read_only_fields = ['slug']

    @staticmethod
    def get_category(obj):
        return obj.category.name

    @staticmethod
    def get_subcategory(obj):
        return obj.subcategory.name

    @staticmethod
    def get_images(obj):
        return {
            'image_200x200': obj.image_200x200,
            'image_600x600': obj.image_600x600,
            'image_1200x1200': obj.image_1200x1200
        }


class SubcategorySerializer(ModelSerializer):
    category = SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'image', 'category']
        read_only_fields = ['slug']

    @staticmethod
    def get_category(obj):
        return obj.category.name


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']
        read_only_fields = ['slug']
