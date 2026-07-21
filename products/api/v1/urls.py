from django.urls import path

from products.api.v1.views import (CategoryViewSet, ProductCreateAPIView,
                                   ProductDestroyAPIView, ProductDetailAPIView,
                                   ProductListAPIView, ProductUpdateAPIView,
                                   SubcategoryViewSet)



urlpatterns = [
    # Category urls
    path('category/create/', CategoryViewSet.as_view({'post': 'create'})),
    path('category/list/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<slug:slug>/detail/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/<slug:slug>/update/', CategoryViewSet.as_view({'patch': 'partial_update', 'put': 'update'})),
    path('category/<slug:slug>/delete/', CategoryViewSet.as_view({'delete': 'destroy'})),
    # Subcategory urls
    path('subcategory/create/', SubcategoryViewSet.as_view({'post': 'create'})),
    path('subcategory/list/', SubcategoryViewSet.as_view({'get': 'list'})),
    path('subcategory/<slug:slug>/detail/', SubcategoryViewSet.as_view({'get': 'retrieve'})),
    path('subcategory/<slug:slug>/update/', SubcategoryViewSet.as_view({'patch': 'partial_update', 'put': 'update'})),
    path('subcategory/<slug:slug>/delete/', SubcategoryViewSet.as_view({'delete': 'destroy'})),
    # Product urls
    path('product/create/', ProductCreateAPIView.as_view()),
    path('product/list/', ProductListAPIView.as_view()),
    path('product/<slug:slug>/detail/', ProductDetailAPIView.as_view()),
    path('product/<slug:slug>/update/', ProductUpdateAPIView.as_view()),
    path('product/<slug:slug>/delete/', ProductDestroyAPIView.as_view()),
]