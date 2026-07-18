from django.urls import path

from products.api.v1.views import (CategoryViewSet, ProductCreateAPIView,
                                   ProductDestroyAPIView, ProductDetailAPIView,
                                   ProductListAPIView, ProductUpdateAPIView,
                                   SubcategoryViewSet)



urlpatterns = [
    # Category urls
    path('category/create/', CategoryViewSet.as_view({'post': 'create'})),
    path('category/list/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/detail/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/<int:pk>/update/', CategoryViewSet.as_view({'put': 'update'})),
    path('category/<int:pk>/delete/', CategoryViewSet.as_view({'delete': 'destroy'})),
    # Subcategory urls
    path('subcategory/create/', SubcategoryViewSet.as_view({'post': 'create'})),
    path('subcategory/list/', SubcategoryViewSet.as_view({'get': 'list'})),
    path('subcategory/<int:pk>/detail/', SubcategoryViewSet.as_view({'get': 'retrieve'})),
    path('subcategory/<int:pk>/update/', SubcategoryViewSet.as_view({'put': 'update'})),
    path('subcategory/<int:pk>/delete/', SubcategoryViewSet.as_view({'delete': 'destroy'})),
    # Product urls
    path('product/create/', ProductCreateAPIView.as_view()),
    path('product/list/', ProductListAPIView.as_view()),
    path('product/<int:pk>/detail/', ProductDetailAPIView.as_view()),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('product/<int:pk>/delete/', ProductDestroyAPIView.as_view()),
]