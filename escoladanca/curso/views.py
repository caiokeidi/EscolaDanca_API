from django.shortcuts import render
from rest_framework import viewsets
from curso.models import Curso, ImagemCurso
from curso.serializers import CursosSerializer, ImagensCursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer

class ImagensCursosViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put']
    queryset = ImagemCurso.objects.all()
    serializer_class = ImagensCursosSerializer
    pagination_class = None
