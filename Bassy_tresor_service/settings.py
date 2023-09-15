"""
Django settings for Bassy_tresor_service project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ='641a0613a98c453a722aed399a87801300f1b1b58acd485097b5d5fd39afa664'
#from decouple import config
#SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "visitor.User"


# Application definition

INSTALLED_APPS = [
    #'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produit',
    'academie',
    'astuce',
    'consultation',
    'visitor',
    'communaute',
    'crispy_forms',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #"whitenoise.middleware.WhiteNoiseMiddleware",
]



ROOT_URLCONF = 'Bassy_tresor_service.urls'
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'Bassy_tresor_service.wsgi.application'
#ASGI_APPLICATION = 'Bassy_tresor_service.asgi.application'
#CHANNEL_LAYERS = {
#    "default": {
#        "BACKEND": "channels_redis.core.RedisChannelLayer",
#        "CONFIG": {
#            "hosts": [("127.0.0.1", 6379)],
#        },
#    },
#}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        "TEST": {
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
}

#DATABASES = {
#    'default':dj_database_url.parse(config('DATABASE_URL'))
#}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL='/Media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'Media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL="/login"

