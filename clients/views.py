from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, ClientContact
from .forms import ClientForm, ClientUpdateForm, ClientContactForm, ClientContactUpdateForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.utils.html import mark_safe


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


class CreateClient(SuccessMessageMixin, CreateView):
    model = Client
    form_class = ClientForm
    # fields = '__all__'  <<------ no aplica porque ya esta incluido en el clientform
    template_name_suffix = '_create_form'
    success_message = "El cliente ha sido creado con exito"


class UpdateClient(UpdateView):
    model = Client
    form_class = ClientUpdateForm
    # fields = '__all__'  <<------ no aplica porque ya esta incluido en el clientform
    template_name_suffix = '_update_form'


class DeleteClient(DeleteView):
    model = Client
    form_class = ClientForm
    # fields = '__all__' <<------ no aplica porque ya esta incluido en el clientform
    # template_name_suffix = '_confirm_delete' <<------por defecto
    success_url = reverse_lazy('clients:client_list')
    success_message = "El cliente ha sido eliminado con exito"
    error_message = "No es posible eliminar al cliente. Esto puede deberse a que: " \
                    "\n - El cliente tiene contactos asociados" \
                    "\n - El cliente tiene cotizaciones asociadas" \
                    "\n - El cliente tiene ventas asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteClient, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('clients:client_list')


# ----------contactos------------
class ClientContactListView(ListView):
    template_name = 'clients/clientcontact_list.html'
    
    def get_queryset(self):
        self.client = get_object_or_404(Client, pk=self.kwargs['pk'])
        return ClientContact.objects.filter(client=self.client)
    
    def get_context_data(self, **kwargs):
        context = super(ClientContactListView, self).get_context_data(**kwargs)
        context["client"] = Client.objects.get(pk=self.kwargs['pk'])
        return context
        


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
    success_message = 'El contacto ha sido creado con exito'


class UpdateClientContact(UpdateView):
    model = ClientContact
    form_class = ClientContactUpdateForm
    # fields = '__all__'
    template_name_suffix = '_update_form'


class DeleteClientContact(DeleteView):
    model = ClientContact
    form_class = ClientContactForm
    # fields = '__all__'
    # template_name_suffix = '_confirm_delete' <<------por defecto
    success_url = reverse_lazy('clients:client_list')
    success_message = "El contacto ha sido eliminado con exito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, mark_safe(self.success_message))
        return super(DeleteClientContact, self).delete(request, *args, **kwargs)
