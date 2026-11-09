from .models import Beneficio
from django import forms

class BeneficioForm(forms.ModelForm):

    class Meta:
        model = Beneficio
        exclude = ()