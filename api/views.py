from rest_framework import viewsets

from api.serializers import UserSerializer, UserAuthSerializer
from api.models import User, UserAuthentication


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class UserAuthViewSet(viewsets.ModelViewSet):
   queryset = UserAuthentication.objects.all()
   serializer_class = UserAuthSerializer
