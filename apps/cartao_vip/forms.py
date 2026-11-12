from django import forms
from .models import Cartao_Vip

class Cartao_VipForm(forms.ModelForm):
    class Meta:
        model = Cartao_Vip
        exclude = ()