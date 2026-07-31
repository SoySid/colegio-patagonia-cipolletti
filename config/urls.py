from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gestion/", include("panel.urls")),
    # Incluimos la app con la tupla (urls, app_name) y registramos el namespace
    path("", include(("escuela.urls", "escuela"), namespace="escuela")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )