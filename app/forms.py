from django import forms
from django.core.exceptions import ValidationError
from . import models

class CreateOrder(forms.ModelForm):

    class Meta:
        model = models.Order

        fields = [ 
            'availability',
            'telefone',
            'user',
            'service', 
        ]
        exclude = [
        ]

