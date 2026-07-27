from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Requisito(models.Model):
    NIVELES = [
        ('PRIMARIO', 'Solo Nivel Primario'),
        ('SECUNDARIO', 'Solo Nivel Secundario'),
        ('AMBOS', 'Ambos Niveles (General)'),
    ]

    nivel = models.CharField(max_length=20, choices=NIVELES, default='AMBOS')
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.get_nivel_display()} - {self.descripcion}"

class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True, null=True)
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asunto} - {self.nombre}"