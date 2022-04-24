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

