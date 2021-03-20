from django.contrib import admin
from escola.models import Professor

class ProfessoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'apelido')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'apelido',)

admin.site.register(Professor, ProfessoresAdmin)