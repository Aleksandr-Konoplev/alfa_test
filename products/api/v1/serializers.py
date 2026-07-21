from rest_framework.fields import SerializerMethodField
from products.api.v1.paginators import NestedSubcategoryPagination
from products.models import Category, Subcategory, Product
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    subcategory = SlugRelatedField(
        slug_field='slug',
        queryset=Subcategory.objects.all()
    )
    images = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'name', 'slug', 'price', 'images']
        read_only_fields = ['slug']

    @staticmethod
    def get_category(obj):
        return obj.subcategory.category.name

    @staticmethod
    def get_subcategory(obj):
        return obj.subcategory.name

    @staticmethod
    def get_images(obj):
        return {
            'image_200x200': obj.image_200x200.url if obj.image else None,
            'image_600x600': obj.image_600x600.url if obj.image else None,
            'image_1200x1200': obj.image_1200x1200.url if obj.image else None,
        }


class SubcategorySerializer(ModelSerializer):
    category = SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'image', 'category']
        read_only_fields = ['slug']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']
        read_only_fields = ['slug']


class CategoryWithSubcategoriesSerializer(ModelSerializer):
    """Список категория с пагинированным списком подкатегорий"""
    subcategories = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'slug', 'image', 'subcategories']

    def get_subcategories(self, obj):
        request = self.context.get('request')
        paginator = NestedSubcategoryPagination()
        paginator.page_size = int(request.query_params.get('sub_page_size', 5))

        sub_qs = obj.subcategories.all()
        page = paginator.paginate_queryset(sub_qs, request)
        if page is not None:
            serializer = SubcategorySerializer(page, many=True, context=self.context)
            return dict([
                ('count', paginator.page.paginator.count),
                ('page_size', paginator.page_size),
                ('page', paginator.page.number),
                ('results', serializer.data),
            ])
        serializer = SubcategorySerializer(sub_qs, many=True, context=self.context)
        return serializer.data