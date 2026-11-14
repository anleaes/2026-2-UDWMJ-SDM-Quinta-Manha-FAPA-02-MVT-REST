from django import forms
from .models import Espectador

class EspectadorForm(forms.ModelForm):

    class Meta:
        model = Espectador
        exclude = ()
        widgets = {
            'data_nascimento': forms.DateInput( attrs={'type': 'date'} ),
            'email': forms.EmailInput( attrs={'type': 'email'} )
        }