from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Noticia, 
    Requisito, 
    Consulta, 
    PostulacionDocente, 
    DatosEscuela, 
    PreguntaFrecuente,
    CarruselInicio,
    Docente
)

# ==========================================
# 1. WIDGETS Y FORMULARIOS AUXILIARES
# ==========================================

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


class CarruselMultipleForm(forms.ModelForm):
    imagenes_multiples = MultipleFileField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        label="Seleccionar varias imágenes juntas (Mantené presionado Ctrl o Shift)",
        required=False
    )

    class Meta:
        model = CarruselInicio
        fields = ['imagenes_multiples', 'imagen', 'titulo', 'subtitulo', 'orden', 'activa']


# ==========================================
# 2. CLASES BASE DE ADMIN
# ==========================================

class ReadOnlyAdmin(admin.ModelAdmin):
    """Clase base para modelos que solo reciben datos desde la web (sin creación manual)."""
    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_add_permission'] = False
        return super().changelist_view(request, extra_context=extra_context)


# ==========================================
# 3. REGISTRO DE MODELOS
# ==========================================

# --- CONFIGURACIÓN DE LA INSTITUCIÓN ---

@admin.register(DatosEscuela)
class DatosEscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'logo_preview')
    search_fields = ('nombre', 'email', 'telefono')
    fieldsets = (
        ('Datos generales', {
            'fields': ('nombre', 'frase', 'logo')
        }),
        ('Inicio', {
            'fields': (
                'hero_tag', 'hero_titulo', 'hero_subtitulo', 'hero_imagen',
                'hero_boton_principal_text', 'hero_boton_principal_url',
                'hero_boton_secundario_text', 'hero_boton_secundario_url'
            )
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono', 'whatsapp', 'email', 'horario')
        }),
        ('Redes sociales', {
            'fields': ('facebook_url', 'instagram_url')
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 40px; max-width: 80px; object-fit: contain;" />', obj.logo.url)
        return "—"

    logo_preview.short_description = 'Logo'


# --- CONTENIDO DE LA WEB ---

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


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'nivel', 'orden', 'activo')
    list_filter = ('nivel', 'activo')
    search_fields = ('nombre', 'cargo')
    list_editable = ('orden', 'activo')


@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden', 'activa')
    list_editable = ('orden', 'activa')


@admin.register(Requisito)
class RequisitoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'nivel')
    list_filter = ('nivel',)
    search_fields = ('descripcion',)
    list_editable = ('nivel',)


# --- RECEPCIÓN DE DATOS / SOLO LECTURA ---

@admin.register(Consulta)
class ConsultaAdmin(ReadOnlyAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto', 'mensaje')


@admin.register(PostulacionDocente)
class PostulacionDocenteAdmin(ReadOnlyAdmin):
    list_display = ('nombre', 'area_materia', 'nivel_interes', 'email', 'telefono', 'fecha_envio', 'revisado')
    list_filter = ('nivel_interes', 'revisado', 'fecha_envio')
    search_fields = ('nombre', 'email', 'area_materia')