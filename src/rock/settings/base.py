import environ
import os
from os.path import abspath, dirname, exists, join

BASE_DIR = dirname(dirname(dirname((abspath(__file__)))))
PROJECT_DIR = join(BASE_DIR, 'rock')
LOCAL_STATIC_CDN_PATH = join(dirname(BASE_DIR), 'static_cdn_test')


# environ, django-environ
env = environ.Env()

env_file = join(PROJECT_DIR, 'settings', 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

SECRET_KEY = env('SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(PROJECT_DIR, 'templates')],
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

WSGI_APPLICATION = 'rock.wsgi.application'
ROOT_URLCONF = 'rock.urls'




# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript)
STATIC_URL = '/static/'

STATIC_ROOT = join(LOCAL_STATIC_CDN_PATH, 'static')

STATICFILES_DIRS = (
    join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

# Media files (Media, Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = join(LOCAL_STATIC_CDN_PATH, 'media_root')
