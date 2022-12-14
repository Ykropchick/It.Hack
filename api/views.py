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


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    parser_classes = (MultiPartParser, FormParser)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)


class StudentFullInfo(APIView):
    def get(self, request):
        search_id = request.GET["id"]
        res = Student.objects.filter(id=search_id)
        if len(res) == 0:
            return Response(None)
        ser = StudentFullSerializer(res[0])
        return Response({"student": ser.data})


class StudentBasicInfo(APIView):
    def get(self, request):
        search_id = request.GET["ID"]
        res = Student.objects.filter(id=search_id)
        if len(res) == 0:
            return Response(None)
        ser = StudentBasicSerializer(res[0])
        return Response({"student": ser.data})


class CompanyFullInfo(APIView):
    def get(self, request):
        search_id = request.GET["ID"]
        res = Company.objects.filter(id=search_id)
        if len(res) == 0:
            return Response(None)
        ser = CompanySerializer(res[0])
        return Response({"user": ser.data})
