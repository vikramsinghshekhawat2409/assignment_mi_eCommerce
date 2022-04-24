from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import *
from .controllers import *
from ecommerce.utility import get_response_object, exception_detail


# Create your views here.
class CategoryViewset(viewsets.ViewSet, CategoryController):
    queryset = Categories.objects.all()

    @action(detail=False, methods=['GET'], url_path='all')
    def get_all_categories(self, request):
        try:
            success, msg, data = self.get_all_categories_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as ex:
            exception_detail()
            res_dict = get_response_object(False, 'Error in getting train data')
        return Response(res_dict, status=status.HTTP_200_OK)
