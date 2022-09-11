from django.urls import include, path
from rest_framework import routers

from .views import SubscribeViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('users/subscriptions/', SubscribeViewSet.as_view({
        'get': 'list'
        }),
        name='subscriptions'
    ),
    path('users/<int:author_id>/subscribe/', SubscribeViewSet.as_view({
        'post': 'create', 'delete': 'delete'
        }),
        name='subscribe'
    ),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
