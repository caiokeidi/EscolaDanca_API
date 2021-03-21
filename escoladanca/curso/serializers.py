from rest_framework import serializers
from curso.models import Curso, ImagemCurso
from django.core.files import File
import base64


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class ImagensCursosSerializer(serializers.ModelSerializer):

    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = ImagemCurso
        fields = ('base64_image', 'id', 'curso')
    
    def get_base64_image(self, obj):
        f = open(obj.foto.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data