from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import ClientListSerializer, ClientDetailSerializer, ClientContactSerializer
from .models import Client, ClientContact
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class ClientView(generics.ListCreateAPIView):
    # queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    # default de rest_framework para agregar filtro al query
    filter_backends = [SearchFilter]
    search_fields = ['client_rut', 'client_name', 'client_giro']

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients.html'
    # override default queryset para que permita hacer filtros. (usando los filtros
    # de rest framework no es necesario, por eso esta commented)

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


    def get(self, request):
        queryset = Client.objects.all()
        return Response({'clients': queryset})


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer


class ClientContactView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class ClientContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer