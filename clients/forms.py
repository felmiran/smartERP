from django import forms
from .models import Client, ClientContact


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'client_rut': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'client_name': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
            'client_giro': forms.TextInput(attrs={'class': 'form control', 'size': '70'}),
            'client_address': forms.TextInput(attrs={'class': 'form control', 'size': '70'}),
            'client_comuna': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'client_ciudad': forms.TextInput(attrs={'class': 'form control', 'size': '20'}),
            'client_region': forms.TextInput(attrs={'class': 'form control', 'size': '10'}),
            'client_tel': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'client_email': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        }


class ClientContactForm(forms.ModelForm):
    class Meta:
        model = ClientContact
        fields = '__all__'
        widgets = {
            '__all__': forms.TextInput(attrs={'class': 'form control col-sm-6', 'size': '16'}),

        }
