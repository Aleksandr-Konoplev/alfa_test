from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from products.api.v1.paginators import CategoryPagination, SubcategoryPagination, ProductPagination
from products.api.v1.serializers import (CategorySerializer, ProductSerializer,
                                         SubcategorySerializer, CategoryWithSubcategoriesSerializer)
from products.models import Category, Product, Subcategory


# --------------------- CRUD Категории --------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_serializer_class(self):
        if self.action == 'with_subcategories':
            return CategoryWithSubcategoriesSerializer
        return CategorySerializer

    @action(detail=False, methods=['get'])
    def with_subcategories(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
