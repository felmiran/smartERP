from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Client(models.Model):
    client_rut = models.CharField(max_length=12, unique=True)
    client_name = models.CharField(max_length=250)
    client_giro = models.CharField(max_length=200)
    client_address = models.CharField(max_length=100)
    client_comuna = models.CharField(max_length=50)
    client_ciudad = models.CharField(max_length=50)
    client_region = models.CharField(max_length=50)
    client_tel = models.CharField(max_length=20, blank=True)
    client_email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)

#    def get_absolute_url(self):
#        return reverse('clients:index')

    class Meta:
        ordering = ['client_rut']

    def __str__(self):
        return self.client_rut + ' - ' + self.client_name


class ClientContact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=250)
    contact_role = models.CharField(max_length=200, blank=True)
    contact_tel = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        ordering = ['contact_name']