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


# inventory movement type
class InventoryMovementTypeListView(ListView):
    template_name = 'payment/inventorymovementtype_list.html'

    def get_queryset(self):
        return InventoryMovementType.objects.all()


class CreateInventoryMovementType(SuccessMessageMixin, CreateView):
    model = InventoryMovementType
    form_class = InventoryMovementTypeForm
    template_name_suffix = '_create_form'
    success_message = "El tipo de movimiento de inventario ha sido creado con exito"


class UpdateInventoryMovementType(UpdateView):
    model = InventoryMovementType
    form_class = InventoryMovementTypeUpdateForm
    template_name_suffix = '_update_form'


class DeleteInventoryMovementType(DeleteView):
    model = InventoryMovementType
    form_class = InventoryMovementTypeForm
    success_url = reverse_lazy('payment:inventorymovementtype_list')
    success_message = "El tipo de movimiento de inventario ha sido eliminado con exito"
    error_message = "No es posible eliminar el tipo de movimiento de inventario. Esto puede deberse a que: " \
                    "\n - El tipo de movimiento de inventario tiene ventas asociadas" \
                    "\n - El tipo de movimiento de inventario tiene compras asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteInventoryMovementType, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('payment:inventorymovementtype_list')


# sale doc type
class SaleDocTypeListView(ListView):
    template_name = 'payment/saledoctype_list.html'

    def get_queryset(self):
        return SaleDocType.objects.all()


class CreateSaleDocType(SuccessMessageMixin, CreateView):
    model = SaleDocType
    form_class = SaleDocTypeForm
    template_name_suffix = '_create_form'
    success_message = "El tipo de documento de ventas ha sido creado con exito"


class UpdateSaleDocType(UpdateView):
    model = SaleDocType
    form_class = SaleDocTypeUpdateForm
    template_name_suffix = '_update_form'


class DeleteSaleDocType(DeleteView):
    model = SaleDocType
    form_class = SaleDocTypeForm
    success_url = reverse_lazy('payment:saledoctype_list')
    success_message = "El tipo de documento de ventas ha sido eliminado con exito"
    error_message = "No es posible eliminar el tipo de documento de ventas. Esto puede deberse a que: " \
                    "\n - El tipo de documento tiene ventas asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteSaleDocType, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('payment:saledoctype_list')


# purchase doc type


# tax
class TaxListView(ListView):
    template_name = 'payment/tax_list.html'

    def get_queryset(self):
        return Tax.objects.all()


class CreateTax(SuccessMessageMixin, CreateView):
    model = Tax
    form_class = TaxForm
    template_name_suffix = '_create_form'
    success_message = "El tipo impuesto ha sido creado con exito"


class UpdateTax(UpdateView):
    model = Tax
    form_class = TaxUpdateForm
    template_name_suffix = '_update_form'


class DeleteTax(DeleteView):
    model = Tax
    form_class = TaxForm
    success_url = reverse_lazy('payment:tax_list')
    success_message = "El tipo de impuesto ha sido eliminado con exito"
    error_message = "No es posible eliminar el tipo de impuesto. Esto puede deberse a que: " \
                    "\n - El tipo de impuesto tiene ventas asociadas"

    def delete(self, request, *args, **kwargs):
        try:
            a = super(DeleteTax, self).delete(request, *args, **kwargs)
            messages.success(self.request, mark_safe(self.success_message))
            return a

        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect('payment:tax_list')