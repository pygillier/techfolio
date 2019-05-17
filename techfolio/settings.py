"""
Django settings for techfolio project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0y%euo)-6v95f$@kmdjpn6_1qv(9!=(1vphtt(avn)qng6oy1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1'
]

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'home.apps.HomeConfig',
    'stackoverflow.apps.StackoverflowConfig',
    'projects.apps.ProjectsConfig',

    # External apps
    'constance',
    'constance.backends.database',
    'sass_processor',
    'crispy_forms',

    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'techfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'techfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'techfolio',
        'USER': 'techfolio_usr',
        'PASSWORD': 'techfolio_pwd',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Constance
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'GITHUB_TOKEN': ('', 'GitHub token for repositories retrieval'),
    'GITHUB_ONLY_USER': (True, "Don't retrieve orgs related repositories"),
    'GITLAB_TOKEN': ('', 'GitLab token for repositories retrieval'),
    'GITLAB_ENDPOINT': ('https://gitlab.com', 'Gitlab instance address'),
    'DEBUG': (False, "Debug mode"),
    'EMAIL_DEFAULT_FROM': ('default@example.com', 'Default sender'),
    'EMAIL_DEFAULT_DEST': ('default@example.com', 'Default recipient'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'GitHub': ('GITHUB_TOKEN', 'GITHUB_ONLY_USER'),
    'GitLab': ('GITLAB_TOKEN', 'GITLAB_ENDPOINT'),
    'Mailings': ('EMAIL_DEFAULT_FROM', 'EMAIL_DEFAULT_DEST'),
    'Misc': ('DEBUG', ),
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Email
SPARKPOST_API_KEY = os.environ.get('SPARKPOST_API_KEY', None)
EMAIL_BACKEND = 'sparkpost.django.email_backend.SparkPostEmailBackend'

# Jet Admin
JET_SIDE_MENU_COMPACT = True

SITE_ID = 1
