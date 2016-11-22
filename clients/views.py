from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, ClientContact
from .forms import ClientForm, ClientContactForm
from django.core.urlresolvers import reverse_lazy

# ----------clientes------------
class ClientListView(ListView):
    template_name = 'clients/client_list.html'

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(DetailView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context["client"] = Client.objects.get(pk=self.kwargs['pk'])
        return context


class CreateClient(CreateView):
    model = Client
    form_class = ClientForm
    # fields = '__all__'  <<------ no aplica porque ya esta incluido en el clientform
    template_name_suffix = '_create_form'


class UpdateClient(UpdateView):
    model = Client
    form_class = ClientForm
    # fields = '__all__'  <<------ no aplica porque ya esta incluido en el clientform
    template_name_suffix = '_update_form'


class DeleteClient(DeleteView):
    model = Client
    form_class = ClientForm
    # fields = '__all__' <<------ no aplica porque ya esta incluido en el clientform
    # template_name_suffix = '_confirm_delete' <<------por defecto
    success_url = reverse_lazy('clients:client_list')


# ----------contactos------------
class ClientContactListView(ListView):
    template_name = 'clients/contact_list.html'
    
    def get_queryset(self, pk):
        return Client.objects.filter(pk=pk)


class ClientContactDetailView(DetailView):
    model = ClientContact
    form_class = ClientContactForm
    template_name = 'clients/contact_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ClientContactDetailView, self).get_context_data(**kwargs)
        context["client"] = Client.objects.get(pk=self.kwargs['pk'])
        context["clientcontact"] = ClientContact.objects.get(pk=self.kwargs['pk2'])
        return context


class CreateClientContact(CreateView):
    model = ClientContact
    form_class = ClientContactForm
    # fields = '__all__'
    template_name_suffix = '_create_form'


class UpdateClientContact(UpdateView):
    model = ClientContact
    form_class = ClientContactForm
    # fields = '__all__'
    template_name_suffix = '_update_form'


class DeleteClientContact(DeleteView):
    model = ClientContact
    form_class = ClientContactForm
    # fields = '__all__'
    template_name_suffix = '_delete_form'