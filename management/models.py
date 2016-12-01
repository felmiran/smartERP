from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Warehouse(models.Model):
    warehouse_code = models.CharField(max_length=10, verbose_name='Codigo Bodega', unique='True')
    warehouse_name = models.CharField(max_length=45, verbose_name='Nombre Bodega')
    warehouse_address = models.CharField(max_length=100, blank=True, verbose_name='Direccion')
    warehouse_comuna = models.CharField(max_length=50, blank=True, verbose_name='Comuna')
    warehouse_ciudad = models.CharField(max_length=50, blank=True, verbose_name='ciudad')
    warehouse_region = models.CharField(max_length=50, blank=True, verbose_name='Region')
    warehouse_tel = models.CharField(max_length=50, blank=True, verbose_name='Telefono')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    def get_absolute_url(self):
        return reverse('management:warehouse_list')

    def __str__(self):
        return self.warehouse_code + ' - ' + self.warehouse_name

    class Meta:
        ordering = ['warehouse_code']


class Branch(models.Model):
    branch_code = models.CharField(max_length=10, verbose_name='Codigo Sucursal', unique='True')
    branch_name = models.CharField(max_length=45)
    branch_address = models.CharField(max_length=100, blank=True)
    branch_comuna = models.CharField(max_length=50, blank=True)
    branch_ciudad = models.CharField(max_length=50, blank=True)
    branch_region = models.CharField(max_length=50, blank=True)
    branch_tel = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('management:branch_list')

    def __str__(self):
        return self.branch_code + ' - ' + self.branch_name

    class Meta:
        ordering = ['branch_code']