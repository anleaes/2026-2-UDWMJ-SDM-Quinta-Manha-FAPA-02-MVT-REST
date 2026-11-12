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
