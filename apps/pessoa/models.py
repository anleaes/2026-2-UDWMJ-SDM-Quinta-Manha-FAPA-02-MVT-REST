from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = models.CharField('Numero de Telefone', max_length=30)
    email = models.EmailField('Email')
    genero = models.CharField('Genero', choices=[('M','Masculino'),('F','Feminino'),('O','Outro/Nao-Informado')], max_length=20)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} - {self.genero}'