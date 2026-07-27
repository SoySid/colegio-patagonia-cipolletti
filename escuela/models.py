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

class DatosEscuela(models.Model):
    nombre = models.CharField(max_length=150, default="Instituto San Martín")
    frase = models.CharField(max_length=255, blank=True, null=True, help_text="Frase institucional o lema de la escuela")
    logo = models.ImageField(upload_to='escuela/logos/', blank=True, null=True, help_text="Logo de la escuela")
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True, help_text="Número sin + ni espacios para el link de WhatsApp")
    email = models.EmailField(blank=True, null=True)
    horario = models.CharField(max_length=150, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Datos de la Escuela"
        verbose_name_plural = "Datos de la Escuela"

    def __str__(self):
        return self.nombre

class PreguntaFrecuente(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    orden = models.IntegerField(default=0, help_text="Número para ordenar la pregunta (menor número aparece primero)")
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Pregunta Frecuente"
        verbose_name_plural = "Preguntas Frecuentes"
        ordering = ['orden']

    def __str__(self):
        return self.pregunta