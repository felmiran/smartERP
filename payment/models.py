# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    payform_name = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.payform_name

    class Meta:
        ordering = ['payform_name']


class CreditCondition(models.Model):
    cond_name = models.CharField(max_length=50, unique=True)
    cond_days = models.PositiveSmallIntegerField(validators=[MaxValueValidator(365), MinValueValidator(0)])
    cond_cuotas = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cond_name

    class Meta:
        ordering = ['cond_name']


class InventoryMovementType(models.Model):
    movement_type_name = models.CharField(max_length=50)
    positive = models.BooleanField(default=True)  # if positive, it adds to product supply. It subtracts otherwise
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.warehouse_name

    class Meta:
        ordering = ['movement_type_name']


class SaleDocType(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_abbr = models.CharField(max_length=10)
    sii_code = models.PositiveSmallIntegerField(choices=DOCS_SII)
    is_active = models.BooleanField(default=True)
    inv_movement_type = models.ForeignKey(InventoryMovementType, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_abbr + ' - ' + self.doc_name

    class Meta:
        ordering = ['doc_abbr']


class PurchaseDocType(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_abbr = models.CharField(max_length=10)
    sii_code = models.PositiveSmallIntegerField(choices=DOCS_SII)
    is_active = models.BooleanField(default=True)
    inv_movement_type = models.ForeignKey(InventoryMovementType, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_abbr + ' - ' + self.doc_name

    class Meta:
        ordering = ['doc_abbr']


class Tax(models.Model):
    tax_name = models.CharField(max_length=30)
    DEC_VALIDATORS = [MaxValueValidator(1, message="Por favor ingrese un numero entre 0 y 1"),
                      MinValueValidator(0, message="Por favor ingrese un numero entre 0 y 1")]
    tax_value = models.DecimalField(max_digits=2, decimal_places=2, validators=DEC_VALIDATORS)

    def __str__(self):
        return self.tax_name

    class Meta:
        ordering = ['tax_name']













