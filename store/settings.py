"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 2.2.12.

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
SECRET_KEY = 'v-p=1b%f=0m5u7@30u&rn4uf#j4yoh=7%jv_mkbvv2rg^sd3_$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'order.apps.OrderConfig',
    'cart.apps.CartConfig',
    'search_app.apps.SearchAppConfig',
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stripe',
    'crispy_forms',
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

ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'shop','templates/'),os.path.join(BASE_DIR,'search_app','templates/'),os.path.join(BASE_DIR,'cart','templates/'),os.path.join(BASE_DIR,'admin','templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store_db',
        'USER':'postgres',
        'PASSWORD':'kitty janindu',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'store/static')
]
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/'

STRIPE_PUBLISHABLE_KEY='pk_test_51GsXtBEaeOts3cccsJEP3ukIMQR8r8WEU9UWceWwkOBoC5WDRvDqGnHGdZBYceuFqzaBEUpPHWI6zwFiwTCBRDer00nzIhCG2p'
STRIPE_SECRET_KEY= 'sk_test_51GsXtBEaeOts3cccGo2y0j5hcS6LZooOhqjN8LHmdOHtT1Az7Sej7QKUrGdTeUeimOXHySSuaaF6EG7ogy1yE0jU00fY4z7Uni'
CRISPY_TEMPLATES_PACK='bootstrap4'
LOGIN_REDIRECT_URL='shop:allProdCat'

#emailmessage settings
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= '587'
EMAIL_USE_TLS= True
EMAIL_HOST_USER='janindur@gmail.com'
EMAIL_HOST_PASSWORD='kitty janindu'

try:
    from local_settings import *
except ImportError:
    pass