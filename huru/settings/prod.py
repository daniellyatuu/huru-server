from .base import *

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huru',
        'USER': 'root',
        'PASSWORD': 'Zomper',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
