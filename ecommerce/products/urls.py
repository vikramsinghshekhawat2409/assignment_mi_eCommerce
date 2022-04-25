from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'category', CategoryViewset)
router.register(r'subcategory', SubCategoryViewset)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path(r'products', ProductsView.as_view()),
]

urlpatterns += router.urls
