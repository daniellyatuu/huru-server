from .base import *

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'www.huruapp.org',
                 'huruapp.org', '192.168.43.155']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'huru',
#         'USER': 'root',
#         'PASSWORD': 'Zomper',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
