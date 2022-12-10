from django.urls import path

from django.urls import include, path

from rest_framework import routers

from api.views import UserAuthViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'AuthUser', UserAuthViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
