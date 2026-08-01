from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    CarruselCreateView,
    CarruselDeleteView,
    CarruselListView,
    CarruselUpdateView,
    ConsultaDeleteView,
    ConsultaListView,
    DatosEscuelaUpdateView,
    DocenteCreateView,
    DocenteDeleteView,
    DocenteListView,
    DocenteUpdateView,
    NoticiaCreateView,
    NoticiaDeleteView,
    NoticiaListView,
    NoticiaUpdateView,
    PostulacionDeleteView,
    PostulacionListView,
    PreguntaFrecuenteCreateView,
    PreguntaFrecuenteDeleteView,
    PreguntaFrecuenteListView,
    PreguntaFrecuenteUpdateView,
    RequisitoCreateView,
    RequisitoDeleteView,
    RequisitoListView,
    RequisitoUpdateView,
    inicio_panel,
)

urlpatterns = [
    # Panel e Ingreso
    path("", inicio_panel, name="panel_inicio"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="panel/login.html"),
        name="panel_login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="panel_logout"),
    # Noticias
    path("noticias/", NoticiaListView.as_view(), name="panel_noticias_lista"),
    path(
        "noticias/nueva/",
        NoticiaCreateView.as_view(),
        name="panel_noticias_crear",
    ),
    path(
        "noticias/editar/<int:pk>/",
        NoticiaUpdateView.as_view(),
        name="panel_noticias_editar",
    ),
    path(
        "noticias/borrar/<int:pk>/",
        NoticiaDeleteView.as_view(),
        name="panel_noticias_borrar",
    ),
    # Requisitos
    path(
        "requisitos/",
        RequisitoListView.as_view(),
        name="panel_requisitos_lista",
    ),
    path(
        "requisitos/nuevo/",
        RequisitoCreateView.as_view(),
        name="panel_requisitos_crear",
    ),
    path(
        "requisitos/editar/<int:pk>/",
        RequisitoUpdateView.as_view(),
        name="panel_requisitos_editar",
    ),
    path(
        "requisitos/borrar/<int:pk>/",
        RequisitoDeleteView.as_view(),
        name="panel_requisitos_borrar",
    ),
    # Docentes
    path("docentes/", DocenteListView.as_view(), name="panel_docentes_lista"),
    path(
        "docentes/nuevo/",
        DocenteCreateView.as_view(),
        name="panel_docentes_crear",
    ),
    path(
        "docentes/editar/<int:pk>/",
        DocenteUpdateView.as_view(),
        name="panel_docentes_editar",
    ),
    path(
        "docentes/borrar/<int:pk>/",
        DocenteDeleteView.as_view(),
        name="panel_docentes_borrar",
    ),
    # Datos de la Escuela
    path(
        "datos-escuela/",
        DatosEscuelaUpdateView.as_view(),
        name="panel_datos_escuela",
    ),
    # Consultas Recibidas
    path(
        "consultas/", ConsultaListView.as_view(), name="panel_consultas_lista"
    ),
    path(
        "consultas/borrar/<int:pk>/",
        ConsultaDeleteView.as_view(),
        name="panel_consultas_borrar",
    ),
    # Preguntas Frecuentes
    path(
        "preguntas/",
        PreguntaFrecuenteListView.as_view(),
        name="panel_preguntas_lista",
    ),
    path(
        "preguntas/nueva/",
        PreguntaFrecuenteCreateView.as_view(),
        name="panel_preguntas_crear",
    ),
    path(
        "preguntas/editar/<int:pk>/",
        PreguntaFrecuenteUpdateView.as_view(),
        name="panel_preguntas_editar",
    ),
    path(
        "preguntas/borrar/<int:pk>/",
        PreguntaFrecuenteDeleteView.as_view(),
        name="panel_preguntas_borrar",
    ),
    # Postulaciones Recibidas
    path(
        "postulaciones/",
        PostulacionListView.as_view(),
        name="panel_postulaciones_lista",
    ),
    path(
        "postulaciones/borrar/<int:pk>/",
        PostulacionDeleteView.as_view(),
        name="panel_postulaciones_borrar",
    ),
    # Carrusel
    path("carrusel/", CarruselListView.as_view(), name="panel_carrusel_lista"),
    path(
        "carrusel/nuevo/",
        CarruselCreateView.as_view(),
        name="panel_carrusel_crear",
    ),
    path(
        "carrusel/editar/<int:pk>/",
        CarruselUpdateView.as_view(),
        name="panel_carrusel_editar",
    ),
    path(
        "carrusel/borrar/<int:pk>/",
        CarruselDeleteView.as_view(),
        name="panel_carrusel_borrar",
    ),
]