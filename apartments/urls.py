from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ApartmentViewSet

router = DefaultRouter()
router.register(r'', ApartmentViewSet, basename='apartment')

urlpatterns = [
    path('', include(router.urls)),
]