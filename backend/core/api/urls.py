from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'service', views.ServiceViewSet)
router.register(r'apartment', views.ApartmentViewSet)

# APIView does not and should not mix with routers
urls = [
    url(r'available-services', views.ApartmentServiceList.as_view()),
    url(r'subscribed-services', views.SubscriptionList.as_view()),
]

urlpatterns = router.urls + urls
