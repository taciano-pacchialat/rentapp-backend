from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', obtain_auth_token, name='auth_login'),
    path('', include(router.urls))
]