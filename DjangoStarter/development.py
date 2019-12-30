from .config import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']

THIRD_PARTY_APPS = [
]

INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE += [
]

