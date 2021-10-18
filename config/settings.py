import os
from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PROJECT_NAME = os.path.basename(BASE_DIR)


SECRET_KEY = 'django-insecure-hzhog)@rhl&u#5@-&@$@9rj2+11strgt0unxwpwu)bp=h#ubvv'

# turn it off !
DEBUG = True

ALLOWED_HOSTS = ["fumi-env.eba-dpaujqmw.ap-northeast-1.elasticbeanstalk.com","isono-law.com","*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # my applications
    'website',
    'contact_form',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)

if "AWS_ACCESS_KEY_ID" in os.environ and "AWS_STORAGE_BUCKET_NAME" in os.environ:
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SIGNATURE_VERSION = 's3v4' 
    AWS_S3_REGION_NAME = "ap-northeast-1"   
    AWS_S3_ENCRYPTION = True
    AWS_S3_HOST = ''
    AWS_IS_GZIPPED = True
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL=os.environ.get('STATIC_URL', default=f'http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com')
else:
    MEDIA_URL = "/images/"
    MEDIA_ROOT = os.path.join(BASE_DIR, 'images/')

# MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'fumi_website_django/static')]
# MEDIA_ROOT = '/var/www/{}/media'.format(PROJECT_NAME)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_API_KEY = '<stripe-api-key>'
STRIPE_PUBLISHABLE_KEY = '<stripe-publishable-key>'

# MAILCHIMP CREDENTIALS
MAILCHIMP_API_KEY = ""
MAILCHIMP_DATA_CENTER = ""
MAILCHIMP_EMAIL_LIST_ID = ""



SENDGRID_API_KEY=""
EMAIL_TEMPLATE_ID = ''
EMAIL_HOST_USER = 'isono@isono-law.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# ----------------------------------------------------------------------------------------




# SERVER_EMAIL = 'ayaoshima0221@gmail.com'

# ----------------------------------------------------------------------------------------
# 詳しくは下記リンク参照。

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.2/ref/settings/

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
