from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from products.api.v1.paginators import CategoryPagination, SubcategoryPagination, ProductPagination
from products.api.v1.serializers import (CategorySerializer, ProductSerializer,
                                         SubcategorySerializer)
from products.models import Category, Product, Subcategory


# --------------------- CRUD Категории --------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


# --------------------- CRUD Подкатегории -----------------
class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = SubcategoryPagination
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


# --------------------- CRUD Продукты ---------------------
class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
