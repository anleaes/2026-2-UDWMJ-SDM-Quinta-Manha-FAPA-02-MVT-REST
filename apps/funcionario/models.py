from decimal import Decimal

from django.db import models
from apps.pessoa.models import Pessoa
from apps.sede.models import Sede

class Funcionario(Pessoa):
    cargo = models.CharField('Cargo', blank=False, null=False, max_length=30)
    sede_de_trabalho = models.ForeignKey(Sede, on_delete=models.CASCADE)
    salario = models.DecimalField('Salário', max_digits=9, decimal_places=2, default=Decimal(0))
    multiplicador_comissao = models.FloatField('Comissão', default=0.0)
    turno_trabalho = models.CharField('Turno de Trabalho', choices=[('M-T','Manhã-Tarde'),('T-N','Tarde-Noite')], max_length=20)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['id']

    def __str__(self):
        return f'{super().nome} - {self.cargo}'