from django.shortcuts import render
from rest_framework import viewsets
from curso.models import Curso, ImagemCurso
from curso.serializers import CursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer


