from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome
    
class ImagemProfessor(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)




