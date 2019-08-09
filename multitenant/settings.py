"""
Django settings for multitenant project.

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
SECRET_KEY = 'qfwea9cz(o490-4(w*cx4t_*j_mww3^6z+7p3ryvj-*_(v&w-*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.localhost']


# Application definition

SHARED_APPS = (
    'django_tenants',  # Obligatorio
    'apps.clientes',  # Se debe listar la app que contiene el modelo que representa al tenant
    'apps.admin',
    'django.contrib.contenttypes',

    # everything below here is optional
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'social_django',

    'bootstrap4',
)

TENANT_APPS = (
    # La siguiente app de Django contrib debe estar TENANT_APPS
    'django.contrib.contenttypes',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    'bootstrap4',

    'apps.mensajes',

)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "clientes.Cliente" # Modelo que hereda de TenantMixin
TENANT_DOMAIN_MODEL = "clientes.Dominio"  # Modelo que hereda de DomainMixin

SITE_ID = 2
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware', # Necesario que este en el top de los MIDDLEWARE
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'multitenant.tenant_urls'
# Con esta línea se tiene una separación de las urls del tenant public  y de las urls para los tenants
PUBLIC_SCHEMA_URLCONF = 'multitenant.public_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request', # Necesario para multitenant
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'multitenant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'multitenant',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# Necesario para multitenant
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

DOMAIN = '.localhost'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_collected')


AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_URL = 'administrador/login'
LOGOUT_URL = 'administrador/logout'
LOGIN_REDIRECT_URL = 'administrador/home'


SOCIAL_AUTH_GITHUB_KEY = 'ab4592b2a5e55d93a4b9'
SOCIAL_AUTH_GITHUB_SECRET = '6cfe527a12e9619b2cdb0cce58ccd541770a07e8'