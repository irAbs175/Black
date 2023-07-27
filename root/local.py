from pathlib import Path
import os


CSRF_TRUSTED_ORIGINS = ["https://8005-irabs175-black-ytaad1kodut.ws-eu102.gitpod.io"]

SECRET_KEY = "django-insecure-cnvj_6xqst#5dhxc1-3^cm06kd7ap81&wr8s@_#)jvju(k6w9v"

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['localhost','8005-irabs175-black-ytaad1kodut.ws-eu102.gitpod.io']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# STATIC FILES (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# STATIC FILES DIRS
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Manifest Static Files Storage is recommended in production, to prevent outdated
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# static root Dir configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

# STATIC URL
STATIC_URL = '/static/'

# Media root Dir configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Media URL
MEDIA_URL = 'media/'