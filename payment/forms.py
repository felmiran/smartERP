from django import forms
from .models import Payform, CreditCondition, InventoryMovementType, SaleDocType, PurchaseDocType, Tax


# payform
class PayformForm(forms.ModelForm):
    model = Payform
    fields = '__all__'
    widgets = {
        'payform_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        'payform_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
    }


class PayformUpdateForm(forms.ModelForm):
    model = Payform
    fields = '__all__'
    widgets = {
        'payform_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
        'payform_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
    }


# credit condition
class CreditConditionForm(forms.ModelForm):
    model = CreditCondition
    fields = '__all__'
    widgets = {
        'cond_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        'cond_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        'cond_days': forms.TextInput(attrs={'class': 'form control', 'size': '4'}),
        'cond_cuotas': forms.TextInput(attrs={'class': 'form control', 'size': '3'}),
    }


class CreditConditionUpdateForm(forms.ModelForm):
    model = CreditCondition
    fields = '__all__'
    widgets = {
        'cond_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
        'cond_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        'cond_days': forms.TextInput(attrs={'class': 'form control', 'size': '4'}),
        'cond_cuotas': forms.TextInput(attrs={'class': 'form control', 'size': '3'}),
    }


# inventory movement type
class InventoryMovementTypeForm(forms.ModelForm):
    model = InventoryMovementType
    fields = '__all__'
    widgets = {
        'movement_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        'movement_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
    }


class InventoryMovementTypeUpdateForm(forms.ModelForm):
    model = InventoryMovementType
    fields = '__all__'
    widgets = {
        'movement_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
        'movement_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
    }


# sale doc type
class SaleDocTypeForm(forms.ModelForm):
    model = SaleDocType
    fields = '__all__'
    widgets = {
        'sdoc_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        'sdoc_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
    }


class SaleDocTypeUpdateForm(forms.ModelForm):
    model = SaleDocType
    fields = '__all__'
    widgets = {
        'sdoc_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
        'sdoc_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
    }


# TODO purchase doc type forms
# purchase doc type


# tax
class TaxForm(forms.ModelForm):
    model = Tax
    fields = '__all__'
    widgets = {
        'tax_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        'tax_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        'tax_value': forms.TextInput(attrs={'class': 'form control', 'size': '4'}),
    }


class TaxUpdateForm(forms.ModelForm):
    model = Tax
    fields = '__all__'
    widgets = {
        'tax_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
        'tax_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        'tax_value': forms.TextInput(attrs={'class': 'form control', 'size': '4'}),
    }