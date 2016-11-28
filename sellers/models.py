from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Seller(models.Model):
    seller_code = models.CharField(max_length=10, verbose_name="Codigo Vendedor")
    seller_name = models.CharField(max_length=50, verbose_name="Nombre Vendedor")
    seller_address = models.CharField(max_length=100, blank=True, verbose_name="Direccion")
    seller_comuna = models.CharField(max_length=50, blank=True, verbose_name="Comuna")
    seller_ciudad = models.CharField(max_length=50, blank=True, verbose_name="Ciudad")
    seller_region = models.CharField(max_length=50, blank=True, verbose_name="Region")
    seller_tel = models.CharField(max_length=50, blank=True, verbose_name="Telefono")
    seller_email = models.EmailField(blank=True, verbose_name="Email")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    def get_absolute_url(self):
        return reverse("sellers:seller_list")

    def __str__(self):
        return self.pk + ' - ' + self.seller_name

    class Meta:
        ordering = ['seller_name']


























