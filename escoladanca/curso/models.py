from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    niveis = models.CharField(max_length=100, blank=False)
    descricao = models.CharField(max_length=300, default='')
    ativo = models.BooleanField(default=True)

class ImagemCurso(models.Model):
    imoveis = models.ForeignKey(Curso, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
