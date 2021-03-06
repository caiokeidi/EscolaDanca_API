from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    niveis = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(max_length=1000, default='')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class ImagemCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
