import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. CONFIGURACIÓN BÁSICA DE RUTA Y SEGURIDAD
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=)%q$4cf7ibo_79$n#lh31x&n%-hy(ci)n0tq^-)20mw^c)qdp'

DEBUG = True

ALLOWED_HOSTS = ['*']


# ==========================================
# 2. APLICACIONES E INTEGRACIONES (INSTALLED APPS)
# ==========================================

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'escuela',
]


# ==========================================
# 3. MIDDLEWARE & RUTAS
# ==========================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# ==========================================
# 4. TEMPLATES Y CONTEXT PROCESSORS
# ==========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'escuela.context_processors.datos_escuela',
            ],
        },
    },
]


# ==========================================
# 5. BASE DE DATOS
# ==========================================

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}


# ==========================================
# 6. VALIDACIÓN DE CONTRASEÑAS
# ==========================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==========================================
# 7. IDIOMA Y ZONA HORARIA
# ==========================================

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# ==========================================
# 8. ARCHIVOS ESTÁTICOS Y MULTIMEDIA (CLOUDINARY)
# ==========================================

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'escuela' / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# Configuración de almacenamiento para Django 4.2+
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Compatibilidad con librerías viejas
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# ==========================================
# 9. PERSISTENCIA DE SESIÓN (STAFF/USUARIOS)
# ==========================================

SESSION_COOKIE_AGE = 86400  # Mantiene la sesión iniciada por 24 horas (en segundos)
SESSION_SAVE_EVERY_REQUEST = True  # Renueva la sesión con cada interacción del usuario
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Mantiene la sesión aunque se cierre la pestaña


# ==========================================
# 10. CORREO ELECTRÓNICO Y PANEL JAZZMIN
# ==========================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'web@colegiopatagonia.edu.ar'

JAZZMIN_SETTINGS = {
    "site_title": "Colegio Patagonia Cipolletti",
    "site_header": "Colegio Patagonia Cipolletti",
    "site_brand": "Patagonia Cipolletti",
    "welcome_sign": "Bienvenido al Sistema del Colegio Patagonia Cipolletti",
    "copyright": "Colegio Patagonia Cipolletti",
}