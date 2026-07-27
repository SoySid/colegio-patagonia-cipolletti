from django.contrib import admin
from .models import Noticia, Requisito, Consulta, DatosEscuela, PreguntaFrecuente

admin.site.register(Noticia)
admin.site.register(Requisito)
admin.site.register(DatosEscuela)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto', 'mensaje')

@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden', 'activa')
    list_editable = ('orden', 'activa')
    search_fields = ('pregunta', 'respuesta')