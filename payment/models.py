from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse


# Create your models here.
DOCS_SII = (
    (30, 'Factura'),
    (32, 'Factura y Servicios no Afectos o Excentos de IVA'),
    (33, 'Factura Electrónica'),
    (34, 'Factura No Afecta o Excenta Electrónica'),
    (35, 'Boleta'),
    (38, 'Boleta Excenta'),
    (39, 'Boleta Electrónica'),
    (41, 'Boleta Excenta Electrónica'),
    (50, 'Guía de Despacho'),
    (52, 'Guía de Despacho Electrónica'),
    (55, 'Nota de Débito'),
    (56, 'Nota de Débito Electrónica'),
    (60, 'Nota de Crédito'),
    (61, 'Nota de Crédito Electrónica'),
    (101, 'Factura de Exportación'),
    (104, 'Nota de Débito de Exportación'),
    (106, 'Nota de Crédito de Exportación'),
    (110, 'Factura de Exportación Electrónica'),
    (111, 'Nota de Débito de Exportación Electrónica'),
    (112, 'Nota de Crédito de Exportación Electrónica'),
    (914, 'Declaración de Importación'),
)


class Payform(models.Model):
    payform_code = models.CharField(max_length=10, verbose_name='Codigo', unique='True')
    payform_name = models.CharField(max_length=30, verbose_name='Codigo Forma de Pago')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    def get_absolute_url(self):
        return reverse('payment:payform_list')

    def __str__(self):
        return self.payform_code + ' - ' + self.payform_name

    class Meta:
        ordering = ['payform_code']


class CreditCondition(models.Model):
    cond_code = models.CharField(max_length=10, verbose_name='Codigo', unique="True")
    cond_name = models.CharField(max_length=50, verbose_name='Nombre Condicion de Pago')
    cond_days = models.PositiveSmallIntegerField(validators=[MaxValueValidator(365), MinValueValidator(0)], verbose_name='Dias')
    cond_cuotas = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)],
                                                   verbose_name='Cuotas')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.cond_code + ' - ' + self.cond_name

    class Meta:
        ordering = ['cond_code']


class InventoryMovementType(models.Model):
    OPERATION = (
        (0, 'Disminuye Inventario'),
        (1, 'Aumenta Inventario'),
    )
    movement_code = models.CharField(max_length=10, verbose_name='Codigo', unique='True')
    movement_name = models.CharField(max_length=50, verbose_name='Nombre Tipo de Movimiento')
    operation = models.PositiveSmallIntegerField(choices=OPERATION, verbose_name='Operacion')  # if 1, it adds to product supply. It subtracts if 0.
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.movement_code + ' - ' + self.movement_name

    class Meta:
        ordering = ['movement_code']


class SaleDocType(models.Model):
    sdoc_code = models.CharField(max_length=10, verbose_name='Codigo', unique='True')
    sdoc_name = models.CharField(max_length=50, verbose_name='Nombre Documento de Venta')
    ssii_code = models.PositiveSmallIntegerField(choices=DOCS_SII, verbose_name='Codigo SII')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    inv_movement_type = models.ForeignKey(InventoryMovementType, on_delete=models.CASCADE,
                                          verbose_name='Tipo de Movimiento')

    def __str__(self):
        return self.sdoc_code + ' - ' + self.sdoc_name

    class Meta:
        ordering = ['sdoc_code']


class PurchaseDocType(models.Model):
    pdoc_code = models.CharField(max_length=10, verbose_name='Codigo', unique='True')
    pdoc_name = models.CharField(max_length=50, verbose_name='Nombre Documento de Compra')
    psii_code = models.PositiveSmallIntegerField(choices=DOCS_SII, verbose_name='Codigo SII')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    inv_movement_type = models.ForeignKey(InventoryMovementType, on_delete=models.CASCADE,
                                          verbose_name='Tipo de Movimiento')

    def __str__(self):
        return self.pdoc_code + ' - ' + self.pdoc_name

    class Meta:
        ordering = ['pdoc_code']


class Tax(models.Model):
    tax_code = models.CharField(max_length=10, verbose_name='Codigo', unique='True')
    tax_name = models.CharField(max_length=30, verbose_name='Nombre Impuesto')
    DEC_VALIDATORS = [MaxValueValidator(100, message="Por favor ingrese un numero entre 0 y 100"),
                      MinValueValidator(0, message="Por favor ingrese un numero entre 0 y 100")]
    tax_value = models.PositiveSmallIntegerField(validators=DEC_VALIDATORS, verbose_name='Monto')

    def __str__(self):
        return self.tax_code + ' - ' + self.tax_name

    class Meta:
        ordering = ['tax_code']













