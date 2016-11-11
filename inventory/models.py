from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from management.models import Warehouse


# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code + ' - ' + self.name

    class Meta:
        ordering = ['code']


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # este code tiene que ser la concatenacion del code de la categoria y subcategoria. eso se ve en el form
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code + ' - ' + self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    # este code tiene que ser la concatenacion del code de la subcategoria y el producto. eso se ve en el form
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # quizas no es necesario. este dato esta almacenado en el model ProductMovement
    updated_unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # quizas no es necesario. este dato esta almacenado en el model ProductMovement
    updated_stock = models.DecimalField(max_digits=8, decimal_places=2)
    # quizas no es necesario. este dato esta almacenado en el model ProductMovement
    updated_stock_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code + ' - ' + self.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class AttributeOption(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=10)

    class Meta:
        unique_together = ('attribute', 'option_name')

    def __str__(self):
        return self.option_name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class ProductMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    inventory_movement_type = models.CharField(max_length=20)
    previous_stock = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.DecimalField(max_digits=8, decimal_places=2)
    out_stock = models.DecimalField(max_digits=8, decimal_places=2)
    updated_stock = models.DecimalField(max_digits=8, decimal_places=2)
    updated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    movement_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # TODO: para que, dependiendo del inv_mov_type, la cantidad se vaya al instock o al outstock. En el fondo,
        # permite validar que ocurre cuando se trata de grabar un form
        # https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.clean

        pass














