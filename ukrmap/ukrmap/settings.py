
from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent


# SECRET_KEY = 'django-insecure-ytu!i+mmblda!wg@36hi(p3hez&=w^k9i(x(hkqehks!*2qkq7'
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = ["*"]

####################
# CUSTOM USER
#####################
AUTH_USER_MODEL = 'user.User'
###########################
# APP
##########################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'corsheaders',
    'django.contrib.gis',

    'rest_framework_simplejwt',
]
#### MY
INSTALLED_APPS += [
    'bknd',
    'map',
    'statistic',
    'organisation',
    'user',
]
##### SPECTACULAR
INSTALLED_APPS +=[
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "corsheaders.middleware.CorsMiddleware",

    "crum.CurrentRequestUserMiddleware",

]

ROOT_URLCONF = 'ukrmap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ukrmap.wsgi.application'


###################################3
# DTB
####################################
# 'ENGINE': 'django.contrib.gis.db.backends.postgis'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.spatialite',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {

        'ENGINE': 'django.contrib.gis.db.backends.postgis',

        'NAME': os.environ.get('DTBNAME'),

        'USER': os.environ.get('DTBUSER'),

        'PASSWORD': os.environ.get('DTBPASSWORD'),

        'HOST': os.environ.get('DTBHOST'),

        'PORT': os.environ.get('DTBPORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


###########################
## TIME ZONE
##########################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




######################
# STATIC MEDIA 
#######################
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

##############################
# CORS
##############################
CORS_ALLOW_ALL_ORIGINS = True


###################################
# DRF
###################################
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        
    ),
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework_gis.schema.GeoFeatureAutoSchema',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # по умолчанию AllowAny IsAuthenticated
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # 'DEFAULT_PAGINATION_CLASS': 'bknd.paginations.BasePagination',

}

###############################
# DRF SPECTACULAR
###############################
SPECTACULAR_SETTINGS = {
    'TITLE': 'Ukr stat API',
    'DESCRIPTION': 'API for Ukraine statistics',
    'VERSION': '1.0.0',

    # auth for api spectacular доступ до апі спектакулар
    # 'SERVE_PERMISSIONS':[
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
    # доступ з можливим токеном для отримання контенту
    'SERVE_AUTHENTICATION':[
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ],

    'SWAGGER_UI_SETTINGS':{
        'DeepLinking':True,
        'DisplayOperationId':True,
    },
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST':True,
    'SORTOPERATIONS':False,
}

######################
# JWT
######################
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("TOKEN",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}