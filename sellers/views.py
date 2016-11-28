from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Seller
from .forms import SellerForm, SellerUpdateForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.html import mark_safe


# Create your views here.
class SellerListView(ListView):
    template_name = 'sellers:seller_list'

    def get_queryset(self):
        return Seller.objects.all()


class CreateSeller(SuccessMessageMixin, CreateView):
    pass


class UpdateSeller(UpdateView):
    pass


class DeleteSeller(DeleteView):
    pass