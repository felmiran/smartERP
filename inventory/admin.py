# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(AttributeOption)
admin.site.register(ProductAttribute)
admin.site.register(ProductMovement)