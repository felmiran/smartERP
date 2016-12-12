# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


# Register your models here.
class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductAttributeValueInline,)


admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductMovement)