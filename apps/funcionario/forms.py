from decimal import Decimal
from django import forms
from .models import Funcionario
from django.core import validators


class FuncionarioForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        validators = [validators.MinValueValidator(Decimal(0))]
        exclude = ()