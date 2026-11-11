from django import forms
from .models import Ingresso

class IngressoForm(forms.ModelForm):
    class Meta:
            model = Ingresso
            exclude = ()