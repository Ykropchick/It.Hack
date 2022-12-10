from rest_framework import serializers
from api.models import *


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        modela = UserAuthentication
        field = (
            "username",
            "email_address"
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "photo"
        )