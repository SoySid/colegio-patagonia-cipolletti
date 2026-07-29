from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos la app con la tupla (urls, app_name) y registramos el namespace
    path('', include(('escuela.urls', 'escuela'), namespace='escuela')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)