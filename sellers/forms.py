from django import forms
from .models import Seller


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        widgets = {
            'seller_code': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'seller_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
            'seller_address': forms.TextInput(attrs={'class': 'form control', 'size': '70'}),
            'seller_comuna': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'seller_ciudad': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'seller_region': forms.TextInput(attrs={'class': 'form control', 'size': '10'}),
            'seller_tel': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'seller_email': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        }


class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        widgets = {
            'seller_code': forms.TextInput(attrs={'class': 'form control', 'size': '15', 'readonly': 'True'}),
            'seller_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
            'seller_address': forms.TextInput(attrs={'class': 'form control', 'size': '70'}),
            'seller_comuna': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'seller_ciudad': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'seller_region': forms.TextInput(attrs={'class': 'form control', 'size': '10'}),
            'seller_tel': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'seller_email': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        }