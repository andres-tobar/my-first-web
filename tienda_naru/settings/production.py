from .base import *


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  'db.sqlite3',
    }
}"""

import dj_database_url
from decouple import config
DATABASE = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )

}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
