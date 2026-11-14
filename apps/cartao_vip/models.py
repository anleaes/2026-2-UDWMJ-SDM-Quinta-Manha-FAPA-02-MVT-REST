from django.db import models
from espectador.models import Espectador
from assinatura.models import Assinatura
from django.utils.crypto import get_random_string
from functools import partial

class Cartao_Vip(models.Model):
    codigo_autenticador = models.CharField(
        'Codigo Autenticador',
        max_length=12,
        default=partial(get_random_string, length=12, allowed_chars='1234567890'),
        unique=True,
        editable=False
    )
    validade = models.DateField('Validade', auto_now=False)
    espectador = models.OneToOneField(Espectador, on_delete=models.CASCADE, related_name='cartao_vip')
    assinatura = models.ForeignKey(Assinatura, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cartao VIP'
        verbose_name_plural = 'Cartões VIP'
        ordering = ['id']

    def __str__(self):
        return f'{self.validade}-{self.codigo_autenticador}'