from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from suppliers.models import Supplier
from payment.models import Payform, CreditCondition, PurchaseDocType
from management.models import Warehouse
from inventory.models import Product


# Create your models here.
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT,
                                  limit_choices_to={'is_active': True})
    payform = models.ForeignKey(Payform, on_delete=models.SET_NULL, blank=True, null=True,
                                limit_choices_to={'is_active': True})
    credit_condition = models.ForeignKey(CreditCondition, on_delete=models.SET_NULL, blank=True, null=True,
                                         limit_choices_to={'is_active': True})
    purchase_doc_type = models.ForeignKey(PurchaseDocType, on_delete=models.SET_NULL, blank=True, null=True,
                                          limit_choices_to={'is_active': True})
    purchase_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=timezone.now, blank=True, null=True,)
    observation = models.TextField(max_length=200, blank=True)
    net_total = models.DecimalField(max_digits=12, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.purchcase_date + ' - ' + self.pk + ' - ' + str(self.supplier.supplier_rut) + ' - ' + \
            str(self.supplier.supplier_name)

    class Meta:
        ordering = ['-purchase_date']


# respecto al on_delete, lo ideal seria que quedara el nombre del payform, o credito condition, o saledoctype,
# en vez de un SET_NULL


class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    observation = models.TextField(max_length=200, blank=True)
    unit_net_cost = models.DecimalField(max_digits=10, decimal_places=2)
    net_total = models.DecimalField(max_digits=12, decimal_places=2)
    taxes = models.DecimalField(max_digits=12, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=12, decimal_places=2)
