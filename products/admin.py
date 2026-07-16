from django.contrib import admin
from .models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'image',)
    search_fields = ('name', 'slug',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'slug',)
    search_fields = ('name', 'slug',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'get_category', 'subcategory', 'slug', 'price',)
    search_fields = ('name', 'slug',)

    @admin.action(description='Категория')
    def get_category(self, obj):
        return obj.subcategory.category
