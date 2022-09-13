from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
]