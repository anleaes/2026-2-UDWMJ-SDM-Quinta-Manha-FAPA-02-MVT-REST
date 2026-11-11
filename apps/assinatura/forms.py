from django import forms
from .models import Assinatura

class AssinaturaForm(forms.ModelForm):

    class Meta:
        model = Assinatura
        exclude = ()