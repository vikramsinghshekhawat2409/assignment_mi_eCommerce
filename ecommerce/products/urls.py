from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'category', CategoryViewset)
router.register(r'subcategory', SubCategoryViewset)

urlpatterns = router.urls
