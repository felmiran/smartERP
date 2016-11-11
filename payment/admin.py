# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Payform)
admin.site.register(CreditCondition)
admin.site.register(InventoryMovementType)
admin.site.register(SaleDocType)
admin.site.register(PurchaseDocType)
admin.site.register(Tax)