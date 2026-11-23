from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        exclude = ('status', 'preco_total', 'ultima_edicao')
        widgets = {
            'ultima_edicao': forms.DateInput(attrs={'type': 'date'})
        }