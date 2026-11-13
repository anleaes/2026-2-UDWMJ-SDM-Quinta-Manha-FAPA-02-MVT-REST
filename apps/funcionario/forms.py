from decimal import Decimal
from django import forms
from .models import Funcionario
from django.core import validators


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        exclude = ()
        widgets = {
            'data_nascimento': forms.DateInput( attrs={'type': 'date'} ),
            'email': forms.EmailInput( attrs={'type': 'email'} )
        }