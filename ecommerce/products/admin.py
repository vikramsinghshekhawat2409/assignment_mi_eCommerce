from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_category_name')
    ordering = ('id',)

    def get_category_name(self, obj):
        return obj.category.name

    get_category_name.short_description = 'Category'


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','get_sub_category_name', 'get_category_name')
    ordering = ('id',)

    def get_sub_category_name(self, obj):
        return obj.subcategory.name

    def get_category_name(self, obj):
        return obj.subcategory.category.name

    get_category_name.short_description = 'Category'
    get_sub_category_name.short_description = 'SubCategory'
