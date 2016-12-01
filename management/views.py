from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Warehouse, Branch
from .forms import WarehouseForm, WarehouseUpdateForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.html import mark_safe
from django.db.models.deletion import ProtectedError


# Create your views here.
class WarehouseListView(ListView):
    template_name = 'management/warehouse_list.html'

    def get_queryset(self):
        return Warehouse.objects.all()


class CreateWarehouse(SuccessMessageMixin, CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name_suffix = '_create_form'
    success_message = "La bodega ha sido creada con exito"


class UpdateWarehouse(UpdateView):
    model = Warehouse
    form_class = WarehouseUpdateForm
    template_name_suffix = '_update_form'


class DeleteWarehouse(DeleteView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy('management:warehouse_list')
    success_message = "La bodega ha sido eliminada con exito"
    error_message = "No es posible eliminar la bodega. Esto puede deberse a que: " \
                    "\n - La bodega tiene ventas asociadas" \
                    "\n - La bodega tiene compras asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteWarehouse, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('management:warehouse_list')

