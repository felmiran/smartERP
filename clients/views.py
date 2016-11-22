from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, ClientContact

# ----------clientes------------
class ClientListView(ListView):
    template_name = 'clients/client_list.html'

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context["client"] = Client.objects.get(pk=self.kwargs['pk'])
        return context


class CreateClient(CreateView):
    model = Client
    fields = '__all__'
    template_name_suffix = '_create_form'


class UpdateClient(UpdateView):
    model = Client
    fields = '__all__'
    template_name_suffix = '_update_form'


class DeleteClient(DeleteView):
    model = Client
    fields = '__all__'
    template_name_suffix = '_delete_form'


# ----------contactos------------
class ClientContactListView(ListView):
    template_name = 'clients/contact_list.html'
    
    def get_queryset(self, pk):
        return Client.objects.filter(pk=pk)


class ClientContactDetailView(DetailView):
    model = ClientContact
    template_name = 'clients/contact_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ClientContactDetailView, self).get_context_data(**kwargs)
        context["client"] = Client.objects.get(pk=self.kwargs['pk'])
        context["clientcontact"] = ClientContact.objects.get(pk=self.kwargs['pk2'])
        return context


class CreateClientContact(CreateView):
    model = ClientContact
    fields = '__all__'
    template_name_suffix = '_create_form'


class UpdateClientContact(UpdateView):
    model = ClientContact
    fields = '__all__'
    template_name_suffix = '_update_form'


class DeleteClientContact(DeleteView):
    model = ClientContact
    fields = '__all__'
    template_name_suffix = '_delete_form'