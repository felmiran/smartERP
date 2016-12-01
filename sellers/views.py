from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Seller
from .forms import SellerForm, SellerUpdateForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.html import mark_safe
from django.db.models.deletion import ProtectedError


# Create your views here.
class SellerListView(ListView):
    template_name = 'sellers/seller_list.html'

    def get_queryset(self):
        return Seller.objects.all()


class CreateSeller(SuccessMessageMixin, CreateView):
    model = Seller
    form_class = SellerForm
    template_name_suffix = '_create_form'
    success_message = "El vendedor ha sido creado con exito"


class UpdateSeller(UpdateView):
    model = Seller
    form_class = SellerUpdateForm
    template_name_suffix = '_update_form'


class DeleteSeller(DeleteView):
    model = Seller
    form_class = SellerForm
    # fields = '__all__' <<------ no aplica porque ya esta incluido en el clientform
    # template_name_suffix = '_confirm_delete' <<------por defecto
    success_url = reverse_lazy('sellers:seller_list')
    success_message = "El vendedor ha sido eliminado con exito"
    error_message = "No es posible eliminar al vendedor. Esto puede deberse a que: " \
                    "\n - El cliente tiene ventas asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteSeller, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('sellers:seller_list')