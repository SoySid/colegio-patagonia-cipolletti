from django.contrib import admin
from .models import Noticia, Requisito, Consulta, PostulacionDocente, DatosEscuela, PreguntaFrecuente

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')

@admin.register(Requisito)
class RequisitoAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'descripcion')
    list_filter = ('nivel',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto', 'mensaje')

@admin.register(PostulacionDocente)
class PostulacionDocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area_materia', 'nivel_interes', 'email', 'telefono', 'fecha_envio', 'revisado')
    list_filter = ('nivel_interes', 'revisado', 'fecha_envio')
    search_fields = ('nombre', 'email', 'area_materia')

@admin.register(DatosEscuela)
class DatosEscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')

@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden', 'activa')
    list_editable = ('orden', 'activa')