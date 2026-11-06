from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = models.CharField('Numero de Telefone')
    email = models.EmailField('Email')
    genero = models.CharField(choices=[('M','Masculino'),('F','Feminino'),('O','Outro/Nao-Informado')])