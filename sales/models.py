from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from clients.models import Client
from payment.models import Payform, CreditCondition, SaleDocType
from sellers.models import Seller
from management.models import Warehouse, Branch
from quotations.models import Quotation
from inventory.models import Product


# Create your models here.
class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT,
                               limit_choices_to={'is_active': True})
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT,
                                  limit_choices_to={'is_active': True})
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT,
                               limit_choices_to={'is_active': True})
    payform = models.ForeignKey(Payform, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    credit_condition = models.ForeignKey(CreditCondition, on_delete=models.PROTECT,
                                         limit_choices_to={'is_active': True})
    sale_doc_type = models.ForeignKey(SaleDocType, on_delete=models.PROTECT,
                                      limit_choices_to={'is_active': True})
    sale_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=timezone.now)
    quotation = models.ForeignKey(Quotation, blank=True, null=True, on_delete=models.SET_NULL)
    observation = models.TextField(max_length=200, blank=True)
    net_total = models.DecimalField(max_digits=12, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.sale_date + ' - ' + self.pk + ' - ' + str(self.client.client_rut) + ' - ' + \
            str(self.client.client_name)

    class Meta:
        ordering = ['-sale_date']


# respecto al on_delete, lo ideal seria que quedara el nombre del payform, o credito condition, o saledoctype,
# en vez de un SET_NULL


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    observation = models.TextField(max_length=200, blank=True)
    unit_net_cost_to_date = models.DecimalField(max_digits=10, decimal_places=2)
    unit_net_price = models.DecimalField(max_digits=10, decimal_places=2)
    net_total = models.DecimalField(max_digits=12, decimal_places=2)
    taxes = models.DecimalField(max_digits=12, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=12, decimal_places=2)





