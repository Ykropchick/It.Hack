from rest_framework import serializers
from api.models import *


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        modela = UserAuthentication
        field = (
            "username",
            "email_address"
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "photo"
        )