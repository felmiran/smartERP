from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Payform, CreditCondition, InventoryMovementType, SaleDocType, PurchaseDocType, Tax
from .forms import (PayformForm, PayformUpdateForm, CreditConditionForm, CreditConditionUpdateForm,
                    InventoryMovementTypeForm, InventoryMovementTypeUpdateForm, SaleDocTypeForm, SaleDocTypeUpdateForm,
                    TaxForm, TaxUpdateForm)
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.html import mark_safe
from django.db.models.deletion import ProtectedError


# payform
class PayformListView(ListView):
    template_name = 'payment/payform_list.html'

    def get_queryset(self):
        return Payform.objects.all()


class CreatePayform(SuccessMessageMixin, CreateView):
    model = Payform
    form_class = PayformForm
    template_name_suffix = '_create_form'
    success_message = "La forma de pago ha sido creada con exito"


class UpdatePayform(UpdateView):
    model = Payform
    form_class = PayformUpdateForm
    template_name_suffix = '_update_form'


class DeletePayform(DeleteView):
    model = Payform
    form_class = PayformForm
    success_url = reverse_lazy('payment:payform_list')
    success_message = "La forma de pago ha sido eliminada con exito"
    error_message = "No es posible eliminar la forma de pago. Esto puede deberse a que: " \
                    "\n - La forma de pago tiene ventas asociadas" \
                    "\n - La forma de pago tiene compras asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeletePayform, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('payment:payform_list')


# credit condition
class CreditConditionListView(ListView):
    template_name = 'payment/creditcondition_list.html'

    def get_queryset(self):
        return CreditCondition.objects.all()


class CreateCreditCondition(SuccessMessageMixin, CreateView):
    model = CreditCondition
    form_class = CreditConditionForm
    template_name_suffix = '_create_form'
    success_message = "La condicion de pago ha sido creada con exito"


class UpdateCreditCondition(UpdateView):
    model = CreditCondition
    form_class = CreditConditionUpdateForm
    template_name_suffix = '_update_form'


class DeleteCreditCondition(DeleteView):
    model = CreditCondition
    form_class = CreditConditionForm
    success_url = reverse_lazy('payment:creditcondition_list')
    success_message = "La condicion de pago ha sido eliminada con exito"
    error_message = "No es posible eliminar la condicion de pago. Esto puede deberse a que: " \
                    "\n - La forma de pago tiene ventas asociadas" \
                    "\n - La forma de pago tiene compras asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteCreditCondition, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('payment:creditcondition_list')