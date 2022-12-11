from rest_framework import serializers
from api.models import *


class StudentFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "skills"
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'