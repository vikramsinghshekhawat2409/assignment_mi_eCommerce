from .models import *
from ecommerce.utility import exception_detail
from .serializers import *


class CategoryController:

    def get_all_categories_details(self, request):
        success = False
        categories_data = {}
        msg = "Error in fetching categories"
        try:
            obj = Categories.objects.filter()
            serializer = CategorySerializer(obj, many=True)
            categories_data = serializer.data
            success = True
            msg = "Success in getting all categories"
        except Exception as e:
            exception_detail()

        return success, msg, categories_data


class SubCategoryController:

    def get_all_subcategories_details(self, request):
        success = False
        sub_categories_data = {}
        msg = "Error in fetching all sub-categories"
        try:
            obj = SubCategories.objects.filter()
            serializer = SubCategorySerializer(obj, many=True)
            sub_categories_data = serializer.data
            success = True
            msg = "Success in getting all sub-categories"
        except Exception as e:
            exception_detail

        return success, msg, sub_categories_data

