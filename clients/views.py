from django.shortcuts import render
from rest_framework import generics
from .serializers import ClientSerializer, ClientContactSerializer
from .models import Client, ClientContact


class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientContactView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class ClientContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer