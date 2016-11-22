from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Client(models.Model):
    client_rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    client_name = models.CharField(max_length=250, verbose_name="Nombre Cliente")
    client_giro = models.CharField(max_length=200, verbose_name="Giro")
    client_address = models.CharField(max_length=100, verbose_name="Direccion")
    client_comuna = models.CharField(max_length=50, verbose_name="Comuna")
    client_ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    client_region = models.CharField(max_length=50, verbose_name="Region")
    client_tel = models.CharField(max_length=20, blank=True, verbose_name="Telefono")
    client_email = models.EmailField(blank=True, verbose_name="E-mail")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        ordering = ['client_rut']

    def get_absolute_url(self):
        return reverse('clients:client_list')

    def __str__(self):
        return self.client_rut + ' - ' + self.client_name


class ClientContact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    contact_name = models.CharField(max_length=250)
    contact_role = models.CharField(max_length=200, blank=True)
    contact_tel = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        ordering = ['contact_name']