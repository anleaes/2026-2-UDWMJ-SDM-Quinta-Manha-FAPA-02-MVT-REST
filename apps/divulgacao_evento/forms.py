from django import forms
from .models import Divulgacao_Evento

class Divulgacao_EventoForm(forms.ModelForm):
    class Meta:
        model = Divulgacao_Evento
        exclude = ()
        widgets = {
            'horario_comeco': forms.TimeInput(attrs={'type': 'time'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time'}),
        }