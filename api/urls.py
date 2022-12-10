from django.urls import path

from django.urls import include, path

from rest_framework import routers

from api.views import UserAuthViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'AuthUser', UserAuthViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
