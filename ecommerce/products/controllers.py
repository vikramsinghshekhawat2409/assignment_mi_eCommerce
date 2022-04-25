from .models import *
from ecommerce.utility import exception_detail
from .serializers import *


class CategoryController:

    def get_all_categories_details(self, request):
        """
        function to get all categories using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
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
        """
        function to get all sub-categories using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
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
            exception_detail()

        return success, msg, sub_categories_data

    def get_sub_category_by_category_details(self, request):
        """
        function to get sub-categories for a given category using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
        success = False
        sub_categories_data = {}
        msg = "Error in fetching sub-categories by a category"
        try:
            category = request.GET.get('category', False)
            if category:
                obj = SubCategories.objects.filter(category__name=category)
                serializer = SubCategorySerializer(obj, many=True)
                sub_categories_data = serializer.data
                success = True
                msg = "Success in getting sub-categories by category"
        except Exception as e:
            exception_detail()

        return success, msg, sub_categories_data


class ProductController:

    def get_all_products_details(self, request):
        """
        function to get all products using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
        success = False
        product_data = {}
        msg = "Error in getting all products"
        try:
            obj = Products.objects.filter()
            serializer = ProductSerializer(obj, many=True)
            product_data = serializer.data
            success = True
            msg = "Success in getting all products"
        except Exception as e:
            exception_detail()

        return success, msg, product_data

    def get_products_by_category_details(self, request):
        """
        function to get all products for a specific category using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
        success = False
        product_data = {}
        msg = "Error in getting products by category"
        try:
            category = request.GET.get('category', False)
            if category:
                obj = Products.objects.filter(subcategory__category__name = category)
                serializer = ProductSerializer(obj, many=True)
                product_data = serializer.data
                success = True
                msg = "Success in getting products by category"
        except Exception as e:
            exception_detail()

        return success, msg, product_data

    def get_products_by_sub_category_details(self, request):
        """
        function to get all products for a specific sub-category using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
        success = False
        product_data = {}
        msg = "Error in getting products by sub-category"
        try:
            sub_category = request.GET.get('sub-category', False)
            if sub_category:
                obj = Products.objects.filter(subcategory__name=sub_category)
                serializer = ProductSerializer(obj, many=True)
                product_data = serializer.data
                success = True
                msg = "Success in getting products by sub-category"
        except Exception as e:
            exception_detail()

        return success, msg, product_data

    def add_product_details(self, request):
        """
        function to add a product for a sub-category using ORM
        :param request: request object
        :return: status with message and the fetched data
        """
        success = False
        product_data = {}
        msg = "Error in adding products"
        try:
            obj = Products()
            product = request.GET.get('product', False)
            if product:
                obj.name = product
            sub_category = request.GET.get('sub-category', False)
            if sub_category:
                obj.subcategory_id = sub_category
            obj.save()

            success = True
            msg = "Success in adding products"
        except Exception as e:
            exception_detail()

        return success, msg, product_data

