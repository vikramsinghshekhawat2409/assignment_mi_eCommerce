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

