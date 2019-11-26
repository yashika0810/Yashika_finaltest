from rest_framework import serializers
from .models import fullname


class fullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model=fullname
        fields="__all__"
