from django.db import models

class Beneficio(models.Model):
    nome = models.CharField('Nome', max_length=20)
    descricao = models.TextField('Descrição', max_length=300)
