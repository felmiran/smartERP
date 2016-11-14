from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import ClientSerializer, ClientContactSerializer
from .models import Client, ClientContact


class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['client_rut', 'client_name', 'client_giro']
    # override default queryset para que permita hacer filtros. usando los filtros
    # de rest framework no es necesario
    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Client.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #                 Q(client_rut__icontains=query) |
    #                 Q(client_name__icontains=query) |
    #                 Q(client_giro__icontains=query)
    #                 ).distinct()
    #     return queryset_list




class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientContactView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class ClientContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer