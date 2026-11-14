from django.db import models
from funcionario.models import Funcionario
from espectador.models import Espectador

class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    pagador = models.ForeignKey(Espectador, on_delete=models.CASCADE)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    ultima_edicao = models.DateField('Data da ultima edição', auto_now=False)
    status = models.CharField('Status', max_length=15, choices=[
        ('A', 'Em Andamento'),
        ('CA', 'Cancelado'),
        ('CO', 'Concluido'),
    ])

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering =['id']

    def __str__(self):
        return f'{self.ultima_edicao}-{self.status}'
