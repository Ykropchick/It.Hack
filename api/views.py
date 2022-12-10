import json

from rest_framework import viewsets

from rest_framework.response import Response
from api.serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from api.models import *
from rest_framework.views import APIView



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentFullSerializer
    parser_classes = (MultiPartParser, FormParser)


class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = UserAuthentication.objects.all()
    serializer_class = UserAuthSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class StudentFullInfo(APIView):
    def get(self, request):
        search_id = request.GET["id"]
        res = Student.objects.filter(id=search_id)
        if len(res) == 0:
            return Response(None)
        ser = StudentFullSerializer(res[0])
        return Response({"user": ser.data})

class StudentBasicInfo(APIView):
    def get(self, request):
        search_id = request.GET["ID"]
        res = Student.object.filter(id=search_id)
        if len(res) == 0:
            return Response(None)
        ser = StudentBasicSerializer(res[0])
        return Response({"user": ser.data})

class CompanyFullInfo(APIView):
    def get(self, request):
        search_id = request.GET["ID"]
        res = Company.object.filter(id=search_id)
        if len(res) == 0:
            return Response(None)
        ser = CompanySerializer(res[0])
        return Response({"user": ser.data})
