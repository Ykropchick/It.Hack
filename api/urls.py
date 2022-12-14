from django.urls import include, path
from rest_framework import routers

from api.views import (CompanyViewSet,
                       StudentViewSet,
                       ProjectViewSet,
                       StudentFullInfo,
                       StudentBasicInfo,
                       CompanyFullInfo)

router = routers.DefaultRouter()
router.register(r'Students', StudentViewSet)
router.register(r'Companies', CompanyViewSet)
router.register(r'Projects', ProjectViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('StudentFullInfo', StudentFullInfo.as_view()),
   path('StudentBasicInfo', StudentBasicInfo.as_view()),
   path('CompanyFullInfo', CompanyFullInfo.as_view())
]
