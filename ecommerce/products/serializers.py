from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='id')
    category = serializers.CharField(source='name')

    class Meta:
        fields = ('category_id', 'category')
        model = Categories


class SubCategorySerializer(serializers.ModelSerializer):
    sub_category_id = serializers.IntegerField(source='id')
    sub_category = serializers.CharField(source='name')
    category = serializers.CharField(source='category.name')

    class Meta:
        fields = ('sub_category_id', 'sub_category', 'category')
        model = SubCategories


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='id')
    product = serializers.CharField(source='name')
    sub_category = serializers.CharField(source='subcategory.name')
    category = serializers.CharField(source='subcategory.category.name')

    class Meta:
        fields = ('product_id', 'product', 'sub_category', 'category')
        model = Products
