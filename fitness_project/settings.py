from pathlib import Path
<<<<<<< HEAD

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-dev-key-change-me'
DEBUG = True
ALLOWED_HOSTS = ["*"]  # pour dev/démo

=======
import os
# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'training',
    'chat',
    'api' ,
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'fitness_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR / 'templates'],  # /templates
=======
        'DIRS': [BASE_DIR / 'templates'],  # Indique à Django de chercher les templates ici
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

<<<<<<< HEAD
WSGI_APPLICATION = 'fitness_project.wsgi.application'
ASGI_APPLICATION = 'fitness_project.asgi.application'

=======
# WSGI and ASGI application
WSGI_APPLICATION = 'fitness_project.wsgi.application'
ASGI_APPLICATION = 'fitness_project.asgi.application'

# Database
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Channels — backend en mémoire (aucun Redis requis pour ta démo)
=======
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# WebSocket configuration
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
# URL pour accéder aux fichiers statiques
STATIC_URL = '/static/'

# Dossier contenant les fichiers statiques de ton projet
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Emplacement où collecter les fichiers statiques avec collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

AUTH_USER_MODEL = 'training.CustomUser'
