from django.db import models
from django.core import validators
from decimal import Decimal
from funcionario.models import Funcionario
from espectador.models import Espectador



class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    pagador = models.ForeignKey(Espectador, on_delete=models.CASCADE)
    preco_total = models.DecimalField(
        'Preço Total', 
        max_digits=10, 
        decimal_places=2, 
        default=Decimal(0), 
        validators=[validators.MinValueValidator(Decimal(0))]
    )
    ultima_edicao = models.DateField('Data da ultima edição', auto_now=True)
    status = models.CharField('Status', max_length=15, default='A', choices=[
        ('A', 'Em Andamento'),
        ('CA', 'Cancelado'),
        ('CO', 'Concluido'),
    ])

    def async_recalcular_preco_total(self):
        self.preco_total = 0
        for ing in self.compra.all():
            self.preco_total += ing.preco_final
        self.save()

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering =['id']

    def __str__(self):
        return f'{self.funcionario} - R${self.preco_total} - {self.status}'
