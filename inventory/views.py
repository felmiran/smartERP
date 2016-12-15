from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Attribute, AttributeValue, Product
from .forms import AttributeValueForm, AttributeValueFormSet
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.utils.html import mark_safe
from django.db import transaction


# ----------attributes------------
class AttributeListView(ListView):
    template_name = 'inventory/attribute_list.html'

    def get_queryset(self):
        return Attribute.objects.all()


class CreateAttribute(CreateView):
    model = Attribute
    # fields = '__all__'
    fields = ['name', ]
    template_name_suffix = '_create_form'
    success_message = "El atributo ha sido creado con exito"

    def get_context_data(self, **kwargs):
        data = super(CreateAttribute, self).get_context_data(**kwargs)
        if self.request.POST:
            data['attributevalues'] = AttributeValueFormSet(self.request.POST)
        else:
            data['attributevalues'] = AttributeValueFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        attributevalues = context['attributevalues']
        with transaction.atomic():
            self.object = form.save()
            
            if attributevalues.is_valid():
                attributevalues.instance = self.object
                attributevalues.save()
        return super(CreateAttribute, self).form_valid(form)


class UpdateAttribute(UpdateView):
    pass


class DeleteAttribute(DeleteView):
    pass


