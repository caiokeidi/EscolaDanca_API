from django.shortcuts import render
from curso.models import Curso, ImagemCurso
from curso.serializers import CursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = .objects.all()
    serializer_class = CursosSerializer


