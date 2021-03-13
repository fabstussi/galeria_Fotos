from django.db import models
from datetime import datetime


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria


class Foto(models.Model):
    imagem = models.FileField(upload_to='galeria')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField(default=datetime.now().strftime('%Y-%m-%d'))
    oculta = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
