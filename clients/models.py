from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


def rut_validate(value):
    validador = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]

    if len(value) == 10 and value.index('-') == 8 and value.count('-') == 1:
        rut = value

    elif len(value) == 9 and value.index('-') == 7 and value.count('-') == 1:
        rut = '0' + value

    else:
        raise ValidationError('Por favor ingrese el rut sin puntos y con guion. Ej. 11111111-1')

    spl_rut = rut.rsplit('-')
    if spl_rut[1] in ('k', 'K'):
        spl_rut.pop()
        spl_rut = spl_rut + ['10']

    elif spl_rut[1] == '0':
        spl_rut.pop()
        spl_rut = spl_rut + ['11']

    rut1 = list(map(int, spl_rut[0]))

    suma = 0
    for i in range(len(spl_rut[0])):
        suma = suma + rut1[-(i+1)]*validador[i]

    if (11 - suma % 11) != int(spl_rut[1]):
        raise ValidationError('El rut que ha ingresado es incorrecto. Por favor intente nuevamente')


# Create your models here.
class Client(models.Model):
    client_rut = models.CharField(max_length=12, unique=True, verbose_name="RUT", validators=[rut_validate])
    client_name = models.CharField(max_length=250, verbose_name="Nombre Cliente")
    client_giro = models.CharField(max_length=200, verbose_name="Giro")
    client_address = models.CharField(max_length=100, verbose_name="Direccion")
    client_comuna = models.CharField(max_length=50, verbose_name="Comuna")
    client_ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    client_region = models.CharField(max_length=50, verbose_name="Region")
    client_tel = models.CharField(max_length=20, blank=True, verbose_name="Telefono")
    client_email = models.EmailField(blank=True, verbose_name="E-mail")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    def get_absolute_url(self):
        return reverse('clients:client_list')

    class Meta:
        ordering = ['client_rut']

    def __str__(self):
        return self.client_rut + ' - ' + self.client_name


class ClientContact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Cliente")
    contact_name = models.CharField(max_length=250, verbose_name="Nombre Contacto")
    contact_role = models.CharField(max_length=200, blank=True, verbose_name="Cargo")
    contact_tel = models.CharField(max_length=20, blank=True, verbose_name="Telefono")
    contact_email = models.EmailField(blank=True, verbose_name="E-Mail")

    def get_absolute_url(self):
        return reverse('clients:client_list')

    class Meta:
        ordering = ['contact_name']

    def __str__(self):
        return self.contact_name
