from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Seller(models.Model):
    seller_name = models.CharField(max_length=50)
    seller_address = models.CharField(max_length=100, blank=True)
    seller_comuna = models.CharField(max_length=50, blank=True)
    seller_ciudad = models.CharField(max_length=50, blank=True)
    seller_region = models.CharField(max_length=50, blank=True)
    seller_tel = models.CharField(max_length=50, blank=True)
    seller_email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.pk + ' - ' + self.seller_name

    class Meta:
        ordering = ['seller_name']


























