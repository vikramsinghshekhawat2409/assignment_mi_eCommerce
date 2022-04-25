from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import *
from .controllers import *
from ecommerce.utility import get_response_object, exception_detail
from django.views.generic import TemplateView

# Create your views here.
class CategoryViewset(viewsets.ViewSet, CategoryController):
    queryset = Categories.objects.all()

    @action(detail=False, methods=['GET'], url_path='all')
    def get_all_categories(self, request):
        """
        function to get all categories
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.get_all_categories_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as ex:
            exception_detail()
            res_dict = get_response_object(False, 'Error in getting categories data')
        return Response(res_dict, status=status.HTTP_200_OK)


class SubCategoryViewset(viewsets.ViewSet, SubCategoryController):
    queryset = SubCategories.objects.all()

    @action(detail=False, methods=['GET'], url_path='all')
    def get_all_subcategories(self, request):
        """
        function to get all sub-categories
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.get_all_subcategories_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as e:
            exception_detail()
            res_dict = get_response_object(False, 'Error in getting all subcategories')
        return Response(res_dict, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='by_category')
    def get_sub_category_by_category(self, request):
        """
        function to get sub-categoreis by a given category
        PARAMS NEED TO PASS :
        {
            "category": ${category_name}
        }
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.get_sub_category_by_category_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as e:
            exception_detail()
            res_dict = get_response_object(False, 'Error in getting subcategories by category')
        return Response(res_dict, status=status.HTTP_200_OK)


class ProductsViewSet(viewsets.ViewSet, ProductController):
    queryset = Products.objects.all()

    @action(detail=False, methods=['GET'], url_path='all')
    def get_all_products(self, request):
        """
        function to get all products
        PARAMS NEED TO PASS :
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.get_all_products_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as e:
            exception_detail()
            res_dict = get_response_object(False, "Error in getting all products")

        return Response(res_dict, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='by_category')
    def get_products_by_category(self, request):
        """
        function to get products by a given category
        {
            "category": ${category_name}
        }
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.get_products_by_category_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as e:
            exception_detail()
            res_dict = get_response_object(False, "Error in getting products by category")

        return Response(res_dict, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='by_sub_category')
    def get_products_by_sub_category(self, request):
        """
        function to get products by a given sub-category
        {
            "sub-category": ${sub_category_name}
        }
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.get_products_by_sub_category_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as e:
            exception_detail()
            res_dict = get_response_object(False, "Error in getting all products by sub_category")

        return Response(res_dict, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='add')
    def add_products(self, request):
        """
        function to add products for a given sub-category
        {
            "product":${product_name}
            "sub-category": ${category_name}
        }
        :param request: request object
        :return: response with status as success and error with message and data.
        """
        try:
            success, msg, data = self.add_product_details(request)
            res_dict = get_response_object(success, msg, data)
        except Exception as e:
            exception_detail()
            res_dict = get_response_object(False, "Error in adding products")

        return Response(res_dict, status=status.HTTP_200_OK)


class ProductsView(TemplateView):
    template_name = "products.html"
