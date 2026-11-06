from django.db import models

class Evento(models.Model):
    name= models.CharField('Nome', max_length=50)
    descricao= models.TextField('Descricao', max_length=200)
    banner= models.ImageField(upload_to='banners',height_field=None, width_field=None, max_length=100)
    regras= models.FileField(upload_to='regras', storage=None, max_length=100)

    class Meta:
        verbose_name= 'Evento'
        verbose_name_plural= 'Eventos'
        ordering= ['id']
