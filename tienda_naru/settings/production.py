from .base import *
import dj_database_url
from decouple import config

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  'db.sqlite3',
    }
}"""

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
