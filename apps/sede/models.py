from django.db import models

class Sede(models.Model):
    nome = models.CharField('Nome-Sede', max_lenght=150, blank=False, null=False)
    endereco = models.CharField('Endereço', max_lenght=250, blank=False, null=False)
    cnpj = models.CharField('CNPJ', max_lenght=100, blank=False, null=False)
    status = models.CharField(choices=[('F','Em Funcionamento'),('X', 'Desativado'),('R', 'Em Reforma')] ,max_lenght=25)
