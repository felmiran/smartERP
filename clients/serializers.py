from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import Client, ClientContact


class ClientListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='clients:clientdetail',
    )
    class Meta:
        model = Client
        fields = (
            'url',
            'client_rut',
            'client_name'
        )


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientContactSerializer(ModelSerializer):
    client = ClientListSerializer()

    class Meta:
        model = ClientContact
        fields = '__all__'
