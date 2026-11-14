from django.db import models
from django.core import validators
from decimal import Decimal
from evento.models import Evento
from sede.models import Sede


class Divulgacao_Evento(models.Model):
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE) 
    local=models.ForeignKey(Sede, on_delete=models.CASCADE)
    data=models.DateField('Data do evento', auto_now=False)
    horario_comeco=models.TimeField("Horario começo",auto_now=False, auto_now_add=False)
    horario_fim=models.TimeField("Horario Fim",auto_now=False, auto_now_add=False)
    preco_base=models.DecimalField(
        'Preço base',
        decimal_places=2,
        max_digits=12,
        default=Decimal(0),
        validators=[validators.MinValueValidator(Decimal(0))]
    )

    class Meta:
        verbose_name = 'Divulgacao Evento'
        verbose_name_plural = "Divulgacao Eventos"
        ordering  =['id']

    def __str__(self):
        return f'{self.evento}'