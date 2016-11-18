from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)
from clients.models import Client, ClientContact


class ClientListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='clients:clientdetail',
    )
    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientContactListSerializer(ModelSerializer):
    # client = ClientListSerializer()
    url = HyperlinkedIdentityField(
        view_name='clients:clientcontactdetail',
    )
    class Meta:
        model = ClientContact
        fields = '__all__'

class ClientContactDetailSerializer(ModelSerializer):
    class Meta:
        model = ClientContact
        fields = '__all__'