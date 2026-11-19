from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        exclude = ()
        widgets = {
            'banner': forms.FileInput(),
            'regras': forms.FileInput()
        }