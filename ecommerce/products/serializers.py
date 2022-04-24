from .models import *
from rest_framework import serializers
from ecommerce.utility import exception_detail


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='id')
    category = serializers.CharField(source='name')

    class Meta:
        fields = ('category_id', 'category')
        model = Categories


