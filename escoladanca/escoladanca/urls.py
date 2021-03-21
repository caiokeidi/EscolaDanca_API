
from django.contrib import admin
from django.urls import path, include
from curso.views import CursosViewSet, ImagensCursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cursos', CursosViewSet, basename='Cursos')
router.register(r'image', ImagensCursosViewSet, basename='Imagens')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    
]
