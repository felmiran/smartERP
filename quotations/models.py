from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from clients.models import Client
from payment.models import Payform, CreditCondition, SaleDocType
from sellers.models import Seller
from inventory.models import Product


# Create your models here.
class Quotation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payform = models.ForeignKey(Payform, on_delete=models.SET_NULL, blank=True, null=True,
                                limit_choices_to={'is_active': True})
    credit_condition = models.ForeignKey(CreditCondition, on_delete=models.SET_NULL, blank=True, null=True,
                                         limit_choices_to={'is_active': True})
    sale_doc_type = models.ForeignKey(SaleDocType, on_delete=models.SET_NULL, blank=True, null=True,
                                      limit_choices_to={'is_active': True})
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True,
                               limit_choices_to={'is_active': True})
    quotation_date = models.DateTimeField(default=timezone.now)
    converted_to_sale = models.BooleanField(default=False)
    observation = models.TextField(max_length=200, blank=True)
    net_total = models.DecimalField(max_digits=12, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.pk + '. ' + str(self.client.client_rut) + ' - ' + str(self.client.client_name)

    class Meta:
        ordering = ['-quotation_date']


# respecto al on_delete, lo ideal seria que quedara el nombre del payform, o credito condition, o saledoctype,
# en vez de un SET_NULL


class QuotationProduct(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    observation = models.TextField(max_length=200, blank=True)
    unit_net_price = models.DecimalField(max_digits=10, decimal_places=2)
    net_total = models.DecimalField(max_digits=12, decimal_places=2)
    taxes = models.DecimalField(max_digits=12, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=12, decimal_places=2)























