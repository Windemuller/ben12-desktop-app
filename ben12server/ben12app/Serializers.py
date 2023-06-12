from rest_framework import serializers
from .models import Client, Record


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [""]
