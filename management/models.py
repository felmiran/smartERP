from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=45)
    warehouse_address = models.CharField(max_length=100, blank=True)
    warehouse_comuna = models.CharField(max_length=50, blank=True)
    warehouse_ciudad = models.CharField(max_length=50, blank=True)
    warehouse_region = models.CharField(max_length=50, blank=True)
    warehouse_tel = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.warehouse_name

    class Meta:
        ordering = ['warehouse_name']


class Branch(models.Model):
    branch_name = models.CharField(max_length=45)
    branch_address = models.CharField(max_length=100, blank=True)
    branch_comuna = models.CharField(max_length=50, blank=True)
    branch_ciudad = models.CharField(max_length=50, blank=True)
    branch_region = models.CharField(max_length=50, blank=True)
    branch_tel = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.branch_name

    class Meta:
        ordering = ['branch_name']