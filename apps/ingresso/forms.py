from django import forms
from .models import Ingresso

class Divulgacao_EventoForm(forms.ModelForm):
    class Meta:
            model = Ingresso
            exclude = ()