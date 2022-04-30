"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ
import redis
from urllib3.util import Retry
import requests

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True),
    SECRET_KEY=(str, '!-ww@kbxor9ag#l^@gphf)o#w9+*b3(zty3ri-@fhdadf6u8j+'),
    REDIS_MINIMUM_EXPIRATION_TIME=(str, '1'),
    X=(str, '10'),
    SHORT_URI_LENGTH=(str, '6'),
    ALLOWED_HOSTS=(list, ['*']),
    CORS_ALLOWED_ORIGIN_REGEXES=(list, [r"^https://\w+\.vivaair\.com$", ]),
    CORS_ORIGIN_ALLOW_ALL=(bool, True),
    DEFAULT_DATABASE=(dict,
                      {
                          'ENGINE': 'django.db.backends.postgresql',
                          'NAME': 'testdb',
                          'USER': 'testuser',
                          'PASSWORD': 'testpassword',
                          'HOST': 'db',
                          'PORT': '5432',
                      }
                      ),
    TIME_ZONE=(str, 'America/Bogota'),
    NAVITAIRE_HOST=(str, "https://dotrezapi.test.vb.navitaire.com"),
    NAVITAIRE_USERNAME=(str, "FPWWWAnonymous"),
    NAVITAIRE_PASSWORD=(str, "Navitaire-4x"),
    NAVITAIRE_DOMAIN=(str, "EXT"),
    NAVITAIRE_CHANNEL_TYPE=(str, "API"),
    NAVITAIRE_MMB_HOST=(str, "https://dotrezapi.test.vb.navitaire.com"),
    NAVITAIRE_MMB_ROLE=(str, "FMMB"),
    PRISMIC_ENDPOINT=(str, "https://vivaair-cms.cdn.prismic.io/api/v2"),
    PRISMIC_TOKEN=(
        str, "MC5ZQm1sWkJJQUFDRUFHVGpW.du-_vTwvK--_ve-_vRvvv73vv71d77-9Ne-_vUzvv73vv73vv71H77-9IO-_vQAx77-9RFph77-977-9WO-_vQ"),
    CYBER_SOURCE_HOST=(str, "https://apis.vivaair.com"),
    AZURE_QUEUE=(str, "Endpoint=sb://vivaair-integration.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=7sX1yL9J+Mh0MpmpmELtb4FPzD4kKHfnVk/VBvbvYgQ="),
    VIVAAIR_IAC=(str, "7709998300040"),
    PAGO_EFECTIVO_URL=(str, "https://cip.pagoefectivo.pe/genpagoif.aspx"),
    ELASTIC_APM_HOST=(str, "https://local-apm.vivaair.com"),
    ELASTIC_APM_SERVICE_NAME=(str, "BOOKING"),
    ELASTIC_APM_SECRET_TOKEN=(str, "7YFDQ3F26hU8HWfb38A03b8o"),
    ELASTIC_APM_ENVIRONMENT=(str, "development"),
    ELASTIC_APM_DEBUG=(bool, True),
    ELASTIC_APM_VERIFY_SERVER_CERT=(bool, False),
    REDIS_HOST=(str, "vivaair-redis-dev.redis.cache.windows.net"),  
    REDIS_PORT=(str, "6380"),
    REDIS_SSL=(bool, True),
    REDIS_DB_CACHE=(int, 0),
    REDIS_PASSWORD=(str, "j2FvcNBUAqI7pYmQ+LauWKKYBjINLkrRIFpH7uboGWY="),
    CONVENIO_BALOTO=(str, "951762"),
    PASSENGERECEIPT_QUEUE=(str, "passenger_receipt_dev"),
    DPLY_VERSION=(str, "-1"),
    AVAILABILITY_HOST=(str, "https://pruebamw.vivaair.com/availability"),
    HTTP_POOL_SIZE=(int, 1),
    DEFAULT_RETRIES=(int, 1),
    REQUEST_TIMEOUT_BOOKING=(int, 20),
    PAYMENT_VIEW_TIMEOUT=(int, 25),
    BUNDLE_REPOSITORY_CACHING_TIME_SECONDS=(int, 300),
    BUNDLE_REPOSITORY_CACHING=(bool, True),
    DEFERRED_PAYMENT_QUEUE=(str, "deferred_shortener_dev"),
    DPN_ACTIVE=(bool, False),
    DPN_ALLOWED_METHODS=(list, ["BL",])
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


REDIS_MINIMUM_EXPIRATION_TIME = env('REDIS_MINIMUM_EXPIRATION_TIME')
X = env('X')
SHORT_URI_LENGTH = env('SHORT_URI_LENGTH')
     
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.staticfiles',
    'rest_framework',
   # 'backend_shared',
    'elasticapm.contrib.django',
    'django.contrib.humanize'
]

MIDDLEWARE = [
    #'conf.middleware.SetRemoteAddrFromForwardedFor', ##  middleware en conf/
    'elasticapm.contrib.django.middleware.TracingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': env('DEFAULT_DATABASE')
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': None,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = env('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#Cors
CORS_ALLOWED_ORIGIN_REGEXES = env("CORS_ALLOWED_ORIGIN_REGEXES")
CORS_ORIGIN_ALLOW_ALL = env("CORS_ORIGIN_ALLOW_ALL")

# EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtprelay.vivaair.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply.reservas@vivaair.com'
EMAIL_HOST_PASSWORD = 'dfrw2os323d2sad'


REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_SSL = env("REDIS_SSL")
REDIS_PASSWORD = env("REDIS_PASSWORD")
REDIS_DB_CACHE = env("REDIS_DB_CACHE")
REDIS_MINIMUM_EXPIRATION_TIME=env("REDIS_MINIMUM_EXPIRATION_TIME")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'ecs': {
            '()': 'ecs_logging.StdlibFormatter'
        }
    },
    'handlers': {
        'elasticapm': {
            'level': 'WARNING',
            'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'ecsconsole': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'ecs'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'propagate': False,
        },
        'business_logic': {
            'level': 'INFO',
            'handlers': ['elasticapm'],
            'propagate': False
        },
        'navitaire': {
            'level': 'INFO',
            'handlers': ['elasticapm'],
            'propagate': False
        },
        'elasticapm.errors': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


DEFERRED_PAYMENT_QUEUE = env("DEFERRED_PAYMENT_QUEUE")
DPN_ACTIVE = env("DPN_ACTIVE")
DPN_ALLOWED_METHODS = env("DPN_ALLOWED_METHODS")
DPLY_VERSION = env("DPLY_VERSION")


REDIS_POOL = redis.BlockingConnectionPool(host=REDIS_HOST,
                                          port='6379',
                                          password=REDIS_PASSWORD,
                                          socket_timeout=30
                                          )




HTTP_POOL_SIZE = env("HTTP_POOL_SIZE")
DEFAULT_RETRIES = env("DEFAULT_RETRIES")
REQUEST_TIMEOUT = env("REQUEST_TIMEOUT_BOOKING")

DEFAULT_TIMEOUT = 5  # seconds


class TimeoutHTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)

SESSION_RETRY = retries = Retry(total=5, backoff_factor=1)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

RETRY_STRATEGY = Retry(total=DEFAULT_RETRIES, backoff_factor=0.5)

class SessionManager(metaclass=Singleton):
    __init=False
    def initialize(self):
        if self.__init: return
        self.session = requests.Session()
        self.session.mount("http://", TimeoutHTTPAdapter(pool_maxsize=HTTP_POOL_SIZE, pool_block=True,
                                                         max_retries=RETRY_STRATEGY, timeout=int(REQUEST_TIMEOUT)))
        self.session.mount("https://", TimeoutHTTPAdapter(pool_maxsize=HTTP_POOL_SIZE, pool_block=True,
                                                          max_retries=RETRY_STRATEGY, timeout=int(REQUEST_TIMEOUT)))
        self.__init = True

    def get(self):
        return self.session


SessionManager().initialize()