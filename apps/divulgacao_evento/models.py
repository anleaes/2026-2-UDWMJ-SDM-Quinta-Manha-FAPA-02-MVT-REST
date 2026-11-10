from django.db import models
from evento.models import Evento
from sede.models import Sede

class Divulgacao_Evento(models.Model):
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE) 
    local=models.ForeignKey(Sede, on_delete=models.CASCADE)
    data=models.DateField('Data do evento', auto_now=False)
    horario_comeco=models.TimeField(auto_now=False, auto_now_add=False)
    horario_fim=models.TimeField(auto_now=False, auto_now_add=False)