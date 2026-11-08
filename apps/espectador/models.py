from django.db import models

from pessoa.models import Pessoa
from sede.models import Sede

class Espectador(Pessoa):
    sede_de_registro = models.ForeignKey(Sede, models.CASCADE)
    ads_por_email = models.BooleanField('Receber ADs por Email', default=True)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    data_ultima_edicao = models.DateTimeField('Última Edição', auto_now=True)

    class Meta:
        verbose_name = 'Espectador'
        verbose_name_plural = 'Espectadores'
        ordering = ['id']
