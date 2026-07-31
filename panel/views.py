from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from escuela.models import (
    CarruselInicio,
    Consulta,
    DatosEscuela,
    Docente,
    Noticia,
    PostulacionDocente,
    PreguntaFrecuente,
    Requisito,
)


class StaffRequeridoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


@staff_member_required
def inicio_panel(request):
    return render(request, "panel/inicio.html")


# ==========================================
# 1. MÓDULO NOTICIAS
# ==========================================
class NoticiaListView(StaffRequeridoMixin, ListView):
    model = Noticia
    template_name = "panel/noticias_lista.html"
    context_object_name = "noticias"
    ordering = ["-fecha_creacion"]


class NoticiaCreateView(StaffRequeridoMixin, CreateView):
    model = Noticia
    fields = ["titulo", "categoria", "descripcion", "imagen"]
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_noticias_lista")


class NoticiaUpdateView(StaffRequeridoMixin, UpdateView):
    model = Noticia
    fields = ["titulo", "categoria", "descripcion", "imagen"]
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_noticias_lista")


class NoticiaDeleteView(StaffRequeridoMixin, DeleteView):
    model = Noticia
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_noticias_lista")


# ==========================================
# 2. MÓDULO REQUISITOS
# ==========================================
class RequisitoListView(StaffRequeridoMixin, ListView):
    model = Requisito
    template_name = "panel/requisitos_lista.html"
    context_object_name = "requisitos"


class RequisitoCreateView(StaffRequeridoMixin, CreateView):
    model = Requisito
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_requisitos_lista")


class RequisitoUpdateView(StaffRequeridoMixin, UpdateView):
    model = Requisito
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_requisitos_lista")


class RequisitoDeleteView(StaffRequeridoMixin, DeleteView):
    model = Requisito
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_requisitos_lista")


# ==========================================
# 3. MÓDULO DOCENTES
# ==========================================
class DocenteListView(StaffRequeridoMixin, ListView):
    model = Docente
    template_name = "panel/docentes_lista.html"
    context_object_name = "docentes"


class DocenteCreateView(StaffRequeridoMixin, CreateView):
    model = Docente
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_docentes_lista")


class DocenteUpdateView(StaffRequeridoMixin, UpdateView):
    model = Docente
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_docentes_lista")


class DocenteDeleteView(StaffRequeridoMixin, DeleteView):
    model = Docente
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_docentes_lista")


# ==========================================
# 4. MÓDULO DATOS DE LA ESCUELA
# ==========================================
class DatosEscuelaUpdateView(StaffRequeridoMixin, UpdateView):
    model = DatosEscuela
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_inicio")

    def get_object(self, queryset=None):
        obj, _ = DatosEscuela.objects.get_or_create(id=1)
        return obj


# ==========================================
# 5. MÓDULO CONSULTAS RECIBIDAS
# ==========================================
class ConsultaListView(StaffRequeridoMixin, ListView):
    model = Consulta
    template_name = "panel/consultas_lista.html"
    context_object_name = "consultas"


class ConsultaDeleteView(StaffRequeridoMixin, DeleteView):
    model = Consulta
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_consultas_lista")


# ==========================================
# 6. MÓDULO PREGUNTAS FRECUENTES
# ==========================================
class PreguntaFrecuenteListView(StaffRequeridoMixin, ListView):
    model = PreguntaFrecuente
    template_name = "panel/preguntas_lista.html"
    context_object_name = "preguntas"


class PreguntaFrecuenteCreateView(StaffRequeridoMixin, CreateView):
    model = PreguntaFrecuente
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_preguntas_lista")


class PreguntaFrecuenteUpdateView(StaffRequeridoMixin, UpdateView):
    model = PreguntaFrecuente
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_preguntas_lista")


class PreguntaFrecuenteDeleteView(StaffRequeridoMixin, DeleteView):
    model = PreguntaFrecuente
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_preguntas_lista")


# ==========================================
# 7. MÓDULO POSTULACIONES RECIBIDAS
# ==========================================
class PostulacionListView(StaffRequeridoMixin, ListView):
    model = PostulacionDocente
    template_name = "panel/postulaciones_lista.html"
    context_object_name = "postulaciones"


class PostulacionDeleteView(StaffRequeridoMixin, DeleteView):
    model = PostulacionDocente
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_postulaciones_lista")


# ==========================================
# 8. MÓDULO CARRUSEL DE PORTADA
# ==========================================
class CarruselListView(StaffRequeridoMixin, ListView):
    model = CarruselInicio
    template_name = "panel/carrusel_lista.html"
    context_object_name = "carrusel"


class CarruselCreateView(StaffRequeridoMixin, CreateView):
    model = CarruselInicio
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_carrusel_lista")


class CarruselUpdateView(StaffRequeridoMixin, UpdateView):
    model = CarruselInicio
    fields = "__all__"
    template_name = "panel/form_generico.html"
    success_url = reverse_lazy("panel_carrusel_lista")


class CarruselDeleteView(StaffRequeridoMixin, DeleteView):
    model = CarruselInicio
    template_name = "panel/borrar_generico.html"
    success_url = reverse_lazy("panel_carrusel_lista")