from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True, help_text="Subir archivo de imagen para la noticia")
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # <-- Corregido acá

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

class PostulacionDocente(models.Model):
    NIVELES = [
        ('MATERNAL', 'Nivel Maternal'),
        ('INICIAL', 'Nivel Inicial'),
        ('PRIMARIO', 'Nivel Primario'),
        ('SECUNDARIO', 'Nivel Secundario'),
        ('VARIOS', 'Varios / General'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    nivel_interes = models.CharField(max_length=20, choices=NIVELES, default='PRIMARIO')
    area_materia = models.CharField(max_length=100, help_text="Ej: Matemática, Maestra de Grado, Inglés, etc.")
    cv = models.FileField(upload_to='cvs/', help_text="Adjuntar archivo PDF o Word")
    mensaje = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    revisado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Postulación Docente"
        verbose_name_plural = "Postulaciones Docentes"

    def __str__(self):
        return f"{self.nombre} - {self.area_materia} ({self.get_nivel_interes_display()})"

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
    hero_tag = models.CharField(max_length=80, blank=True, null=True, default="Inscripciones Abiertas", help_text="Texto corto del banner principal")
    hero_titulo = models.CharField(max_length=150, blank=True, null=True, default="EDUCACIÓN INTEGRAL Y DE EXCELENCIA")
    hero_subtitulo = models.TextField(blank=True, null=True, default="Propuesta pedagógica comprometida con una formación humana de calidad desde Nivel Maternal hasta Primario.")
    hero_imagen = models.ImageField(upload_to='escuela/hero/', blank=True, null=True, help_text="Imagen principal del inicio")
    hero_boton_principal_text = models.CharField(max_length=80, blank=True, null=True, default="VER REQUISITOS DE INSCRIPCIÓN")
    hero_boton_principal_url = models.CharField(max_length=255, blank=True, null=True, default="/requisitos/")
    hero_boton_secundario_text = models.CharField(max_length=80, blank=True, null=True, default="CONTACTANOS")
    hero_boton_secundario_url = models.CharField(max_length=255, blank=True, null=True, default="/contacto/")

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

class BloqueInicio(models.Model):
    titulo = models.CharField(max_length=120, verbose_name="Título")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    icono = models.CharField(max_length=40, blank=True, null=True, verbose_name="Icono", help_text="Ejemplo: ✨, 📚, 🏫")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden")
    activa = models.BooleanField(default=True, verbose_name="¿Mostrar en la web?")

    class Meta:
        verbose_name = "Bloque de Inicio"
        verbose_name_plural = "Bloques de Inicio"
        ordering = ['orden']

    def __str__(self):
        return self.titulo

class CarruselInicio(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Título (Opcional)")
    subtitulo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Subtítulo / Bajada (Opcional)")
    imagen = models.ImageField(upload_to='carrusel/', blank=True, null=True, verbose_name="Imagen del Carrusel")
    orden = models.PositiveIntegerField(default=0, help_text="Orden de aparición (0, 1, 2...)")
    activa = models.BooleanField(default=True, verbose_name="¿Mostrar en la web?")

    class Meta:
        verbose_name = "Imagen del Carrusel"
        verbose_name_plural = "Carrusel del Inicio"
        ordering = ['orden']

    def __str__(self):
        return self.titulo or f"Imagen {self.id}"

class Docente(models.Model):
    NIVELES = [
        ('DIRECTIVO', 'Equipo Directivo'),
        ('INICIAL', 'Nivel Inicial / Maternal'),
        ('PRIMARIO', 'Nivel Primario'),
        ('ESPECIALIDAD', 'Especialidades / Talleres'),
    ]

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, help_text="Ej: Directora, Docente de Inglés, etc.")
    nivel = models.CharField(max_length=20, choices=NIVELES, default='PRIMARIO')
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)
    orden = models.IntegerField(default=0, help_text="Para ordenar quién sale primero")
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"