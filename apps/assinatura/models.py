from decimal import Decimal
from django.core import validators
from django.db import models

from beneficio.models import Beneficio

class Assinatura(models.Model):
    icone = models.ImageField('Ícone', upload_to='icones')
    nome =  models.CharField('Nome', max_length=25)
    descricao = models.TextField('Descrição', max_length=300)
    custo_mensal = models.DecimalField('Custo Mensal', decimal_places=2, max_digits=9, default=Decimal(0), validators=[validators.MinValueValidator(Decimal(0))])
    beneficios = models.ManyToManyField(Beneficio, verbose_name='Beneficios')

    class Meta:
        verbose_name = 'Assinatura'
        verbose_name_plural = 'Assinaturas'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} - R$ {self.custo_mensal}'