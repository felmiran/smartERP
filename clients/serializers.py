from rest_framework import serializers
from .models import Client, ClientContact


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientContactSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ClientContact
        fields = '__all__'
