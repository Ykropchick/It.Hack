from rest_framework import viewsets

from api.serializers import StudentSerializer, UserAuthSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from api.models import Student, UserAuthentication


class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   parser_classes = (MultiPartParser, FormParser)


class UserAuthViewSet(viewsets.ModelViewSet):
   queryset = UserAuthentication.objects.all()
   serializer_class = UserAuthSerializer
