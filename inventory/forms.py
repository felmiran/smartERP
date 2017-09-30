from django import forms
from django.forms.models import inlineformset_factory

from .models import Attribute, AttributeValue


class AttributeValueForm(forms.ModelForm):
    class Meta:
        model = AttributeValue
        exclude = ()


class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form control', 'size': '15'}),
            'description': forms.TextInput(attrs={'class': 'form control', 'size': '30'}),
        }


AttributeValueFormSet = inlineformset_factory(Attribute, AttributeValue, form=AttributeValueForm, extra=1)

