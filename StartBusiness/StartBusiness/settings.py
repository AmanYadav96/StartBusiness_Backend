
from pathlib import Path
import os
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+7n!)oo$i!4@xjas+iqs$9q6a5d0_4l82h$=&tl#74wyywv3l('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*","0.0.0.0:0","https://start-business-46u6138wk-amanyadav96s-projects.vercel.app/","https://start-business.vercel.app/","https://start-business-agq8n22nb-amanyadav96s-projects.vercel.app","startbusinessbackend-production.up.railway.app","https://web-zt9gb9h7cogx.up-sg-sin1-k8s-1.apps.run-on-seenode.com"]

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'drf_yasg',
    'django_filters',
    'channels',
    'user',
    'contractor',
    'manager',
    'category',
    'brand',
    'dealer',
    'product',
    'product_highlight',
    'stock',
    'address',
    'compare',
    'cart',
    'order',
    'wishlist',
    'payment',
    'invoice',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StartBusiness.urls'

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

WSGI_APPLICATION = 'StartBusiness.wsgi.application'
ASGI_APPLICATION = 'StartBusiness.asgi.application'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Mongodb
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'sb',
#         'CLIENT': {
#             # 'host': 'mongodb+srv://aman:aman@cluster0.th0tbxg.mongodb.net/?retryWrites=true&w=majority',
#             'host': 'localhost',
#         },
#     }
# }
# postgres localhost
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'krishnadb',
        'USER': 'avnadmin',
        'PASSWORD': 'AVNS_erbznMFI6oik4jMdSZN',
        'HOST': 'krishna-myproject456.j.aivencloud.com',
        'PORT': '23642',
    }
}


# Postgres Animal
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'USER':'admin',
#         'NAME': 'postgres',
#         'PASSWORD': 'HmG5FrMQdrZkcvFPm45E5VufdcB15t',
#         'HOST': 'ap-south-1.cfbeb907-e693-49d5-af93-44d7dae2e8bc.aws.ybdb.io',
#         'PORT': '5433',
#     }
# }
import redis


CELERY_BROKER_URL ='rediss://default:AVNS_dDCXi2vGmyRQcefboRh@redis-2b6e85c-virajgurjar789-c014.l.aivencloud.com:12875'
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE='US/Pacific'
TIME_ZONE = 'US/Pacific'
USE_TZ = True

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}
AUTH_USER_MODEL = 'user.User'


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': "secret",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "user_id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",
}
# rest framework settings ________________________________________________________________
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
      
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

DJANGO_ALLOW_ASYNC_UNSAFE=True


CACHE_TTL = 60 * 1500
import redis

# r = redis.Redis(
#   host='redis-18755.c16.us-east-1-3.ec2.redns.redis-cloud.com',
#   port=18755,
#   password='XmKdA05qIKuC4HoCyZ39YkLlFNdCl0mK')
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://default:XmKdA05qIKuC4HoCyZ39YkLlFNdCl0mK@redis-18755.c16.us-east-1-3.ec2.redns.redis-cloud.com:18755',
        # 'LOCATION': 'redis://127.0.0.1:6379/1', 
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SERIALIZER': 'django_redis.serializers.json.JSONSerializer',  # Optional, JSON serializer
        }
    }
}


#AWS_CREDINTIALS

# AWS_ACCESS_KEY_ID = 'AKIAYYNHA3KRGX66HUTL'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'sangeetamarble'
# AWS_S3_REGION_NAME = 'ap-south-1'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# settings.py
# from google.oauth2 import service_account
    
# # ...
    
# GS_BUCKET_NAME = "snagitamarble2" 
    
# DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    
# MEDIA_URL = "URL.to.GCS/"

# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     "krishna-project-423910-0657a7f1bdc9.json"
# )
# GS_EXPIRATION = timedelta(minutes=5)
    
# GS_BLOB_CHUNK_SIZE = 1024 * 256 * 40

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL':'cloudinary://288782735175668:geU7eWiYmQBFDHXJN3_iWia3IJE@dynvzncn2',
    'CLOUD_NAME': 'dynvzncn2',
    'API_KEY': '288782735175668',
    'API_SECRET': 'geU7eWiYmQBFDHXJN3_iWia3IJE'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'