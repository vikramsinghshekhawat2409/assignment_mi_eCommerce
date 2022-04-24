from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'category', CategoryViewset)

urlpatterns = router.urls
