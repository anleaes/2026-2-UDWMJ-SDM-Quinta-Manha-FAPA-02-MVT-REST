from django import forms
from .models import Espectador

class EspectadorForm(forms.ModelForm):

    class Meta:
        model = Espectador
        exclude = ()