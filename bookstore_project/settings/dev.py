from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS += [
  
    'debug_toolbar',
    
]




MIDDLEWARE += [

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),                      
        'USER': config('D_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('PORT')
    }
}






# django-debug-toolbar
INTERNAL_IPS = ['127.0.0.1',]
