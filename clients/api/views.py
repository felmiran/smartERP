from rest_framework import generics, views
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

from clients.api.serializers import (
    ClientListSerializer,
    ClientDetailSerializer,
    ClientContactListSerializer,
    ClientContactDetailSerializer
)

from clients.models import Client, ClientContact


# list clients/ create new client
class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientListSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Client.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_rut__icontains=query) |
                    Q(client_name__icontains=query) |
                    Q(client_giro__icontains=query)
                    ).distinct()
        return queryset_list


# display/update/delete client
class ClientDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer

# list client contacts/ create new client contact
class ClientContactListCreateView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactListSerializer


class ClientContactDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactDetailSerializer

