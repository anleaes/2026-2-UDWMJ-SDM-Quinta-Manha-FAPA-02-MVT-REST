from django import forms
from .models import Cupom

class CupomForm(forms.ModelForm):
    class Meta:
        model = Cupom
        exclude = ()
        widgets = {
            'data_vencimento': forms.DateInput(attrs={"type": "date"})
        }