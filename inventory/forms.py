from django import forms
from django.forms.models import inlineformset_factory

from .models import Attribute, AttributeValue, Product


class AttributeValueForm(forms.ModelForm):
    class Meta:
        model = AttributeValue
        exclude = ()

AttributeValueFormSet = inlineformset_factory(Attribute, AttributeValue, form=AttributeValueForm, extra=1)

