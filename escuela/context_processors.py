from .models import DatosEscuela

def datos_escuela(request):
    # Trae el primer registro de la configuración o None si no se creó aún
    config = DatosEscuela.objects.first()
    return {'escuela_info': config}