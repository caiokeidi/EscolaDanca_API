from django.contrib import admin
from curso.models import Curso, ImagemCurso

class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Curso, CursosAdmin)
admin.site.register(ImagemCurso)
