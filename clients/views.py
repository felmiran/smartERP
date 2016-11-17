from rest_framework import generics
from .serializers import ClientListSerializer, ClientDetailSerializer, ClientContactSerializer
from .models import Client, ClientContact
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clientdetail.html'

    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = ClientDetailSerializer(client)
        return Response({'serializer': serializer, 'client': client})

    def post(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = ClientListSerializer(client, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'client': client})
        serializer.save()
        return redirect('clients:clients')


class ClientView(generics.ListAPIView):
    serializer_class = ClientListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients.html'

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


class ClientContactView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class ClientContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer