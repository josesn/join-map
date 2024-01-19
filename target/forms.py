from django import forms
from django.forms import TextInput, DateInput

from .models import Target

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'geocode', 'expire_date']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Name'
                }),
            'geocode': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 400px;',
                'placeholder': 'Ex: -3.7899621,-38.6015098'
                }),
            'expire_date': DateInput(attrs={
                'type': 'date',
                'class': "form-control", 
                'style': 'max-width: 200px; padding: 5px',
                'placeholder': 'Expira em'
                })
        }