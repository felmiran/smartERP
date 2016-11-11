from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Supplier(models.Model):
    supplier_rut = models.CharField(max_length=12, unique=True)
    supplier_name = models.CharField(max_length=250)
    supplier_giro = models.CharField(max_length=200)
    supplier_address = models.CharField(max_length=100)
    supplier_comuna = models.CharField(max_length=50)
    supplier_ciudad = models.CharField(max_length=50)
    supplier_region = models.CharField(max_length=50)
    supplier_tel = models.CharField(max_length=20, blank=True)
    supplier_email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)

#    def get_absolute_url(self):
#        return reverse('clients:index')

    def __str__(self):
        return self.rut_empresa + ' - ' + self.nombre_empresa

    class Meta:
        ordering = ['supplier_rut']


class SupplierContact(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=250)
    contact_role = models.CharField(max_length=200, blank=True)
    contact_tel = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        ordering = ['contact_name']