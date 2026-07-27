from django.contrib import admin
from .models import Noticia, Requisito, Consulta

admin.site.register(Noticia)
admin.site.register(Requisito)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto', 'mensaje')