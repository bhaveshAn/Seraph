import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#SECRET_KEY = 'asdfghjklkjhgfdsdfghjkl,kjhgfdsdfghjkjhgfdsdfghjkjhgfdsdfghj'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Extract data from `conf/secrets.json`
'''
try:
    secrets_file = os.path.join(DATA_DIR, 'conf', 'secrets.json')
    with open(secrets_file, 'r') as handle:
        SECRETS = json.load(handle)
except IOError:
    raise IOError('Config file (`data/conf/secrets.json`) not found.')
'''

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = SECRETS.get('secret_key')
SECRET_KEY = 'v(uku#op7!2r-eel^l&gg!xqvs-phjc$)4a4(^a&%l999@39w!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = SECRETS.get('allowed_hosts', [])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'companies.apps.CompaniesConfig',
    'employees.apps.EmployeesConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'seraph.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'seraph', 'templates')],
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


WSGI_APPLICATION = 'seraph.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
#STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Media
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/employees/login/'


# Auth user model
# AUTH_USER_MODEL = 'teams.Team'

# Media and Static Roots
MEDIA_ROOT = os.path.join(DATA_DIR, 'media_root')
STATIC_ROOT = os.path.join(DATA_DIR, 'static_root')