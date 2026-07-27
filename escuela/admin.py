from django import forms
from django.contrib import admin
from .models import (
    Noticia, 
    Requisito, 
    Consulta, 
    PostulacionDocente, 
    DatosEscuela, 
    PreguntaFrecuente, 
    CarruselInicio
)


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


# WIDGET PERSONALIZADO QUE HABILITA LA SELECCIÓN MÚLTIPLE EN DJANGO
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        if data in (None, ""):
            return []

        if isinstance(data, (list, tuple)):
            return [super().clean(item, initial) for item in data if item not in (None, "")]

        return [super().clean(data, initial)]


# FORMULARIO PARA CARGA MÚLTIPLE DE IMÁGENES
class CarruselMultipleForm(forms.ModelForm):
    imagenes_multiples = MultipleFileField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        label="Seleccionar varias imágenes juntas (Mantené presionado Ctrl o Shift)",
        required=False
    )

    class Meta:
        model = CarruselInicio
        fields = ['imagenes_multiples', 'imagen', 'titulo', 'subtitulo', 'orden', 'activa']


@admin.register(CarruselInicio)
class CarruselInicioAdmin(admin.ModelAdmin):
    form = CarruselMultipleForm
    list_display = ('id', 'titulo', 'orden', 'activa')
    list_editable = ('orden', 'activa')
    save_as = True

    def save_model(self, request, obj, form, change):
        archivos = form.cleaned_data.get('imagenes_multiples', [])

        if archivos:
            for i, f in enumerate(archivos):
                CarruselInicio.objects.create(
                    imagen=f,
                    titulo=obj.titulo or f"Imagen {i+1}",
                    subtitulo=obj.subtitulo,
                    orden=obj.orden + i,
                    activa=obj.activa
                )
        else:
            super().save_model(request, obj, form, change)