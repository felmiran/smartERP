from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, ClientContact


class ClientListView(ListView):
    template_name = 'clients/client_list.html'

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'