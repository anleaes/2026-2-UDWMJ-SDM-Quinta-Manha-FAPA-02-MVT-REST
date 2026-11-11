from django.db import models
from espectador.models import Espectador
from divulgacao_evento.models import Divulgacao_Evento
from cupom.models import Cupom

class Ingresso(models.Model):
    espectador = models.ForeignKey(Espectador, on_delete=models.CASCADE)
    evento_divulgado = models.ForeignKey(Divulgacao_Evento, on_delete=models.CASCADE)
    cupom_aplicado = models.ForeignKey(Cupom, on_delete=models.CASCADE)
