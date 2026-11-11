from django.db import models
from espectador.models import Espectador
from divulgacao_evento.models import Divulgacao_Evento
from cupom.models import Cupom
from venda.models import Venda

class Ingresso(models.Model):
    espectador = models.ForeignKey(Espectador, on_delete=models.CASCADE)
    evento_divulgado = models.ForeignKey(Divulgacao_Evento, on_delete=models.CASCADE)
    cupom_aplicado = models.ForeignKey(Cupom, on_delete=models.CASCADE)
    venda= models.ForeignKey(Venda, on_delete=models.CASCADE)
    validado = models.BooleanField('Validado', default=False)


    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = "Ingressos"
        ordering  =['id']

    def __str__(self):
        return f'{self.validado}'