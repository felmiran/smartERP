from django import forms
from .models import Warehouse, Branch


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'
        widgets = {
            'warehouse_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'warehouse_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
            'warehouse_address': forms.TextInput(attrs={'class': 'form control', 'size': '70'}),
            'warehouse_comuna': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'warehouse_ciudad': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'warehouse_region': forms.TextInput(attrs={'class': 'form control', 'size': '10'}),
            'warehouse_tel': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        }


class WarehouseUpdateForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'
        widgets = {
            'warehouse_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
            'warehouse_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
            'warehouse_address': forms.TextInput(attrs={'class': 'form control', 'size': '70'}),
            'warehouse_comuna': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'warehouse_ciudad': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'warehouse_region': forms.TextInput(attrs={'class': 'form control', 'size': '10'}),
            'warehouse_tel': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
        }
