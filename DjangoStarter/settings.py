import os
from decouple import config

if config('IS_DEVELOPMENT'):
    from .development import *
else:
    from .production import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


ROOT_URLCONF = 'DjangoStarter.urls'

WSGI_APPLICATION = 'DjangoStarter.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# Authentication urls
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
# End Authentication Urls

# for sending email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# User can login by their email and username
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
]
