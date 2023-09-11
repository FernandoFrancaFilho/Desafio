from rest_framework import routers
from .views import CarroViewSet, CnhViewSet

router = routers.DefaultRouter()
router.register(r'cnhs', CnhViewSet)
router.register(r'carros', CarroViewSet) 
     
urlpatterns = router.urls