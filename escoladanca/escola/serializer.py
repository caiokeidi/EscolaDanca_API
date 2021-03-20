from rest_framework import serializers
from curso.models import Curso

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'