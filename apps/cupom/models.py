from django.db import models
from django.core import validators
from evento.models import Evento


# Create your models here.
class Cupom(models.Model):
    porcentagem_desconto=models.IntegerField(
        'Porcentagem de desconto', 
        blank=False,
        null=False,
        default=0,
        validators=[validators.MinValueValidator(0)]
        )
    data_vencimento=models.DateField('Data de vencimento', auto_now=False)
    eventos_validos=models.ManyToManyField(Evento, verbose_name="Eventos")

    class Meta:
        verbose_name= 'Cupom'
        verbose_name_plural = 'Cupons'
        ordering = ['id']

    def __str__(self):
        return f'{self.porcentagem_desconto}-{self.data_vencimento}'