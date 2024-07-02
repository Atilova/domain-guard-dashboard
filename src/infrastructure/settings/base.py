from config import conf

from pathlib import Path


# PLACE HERE DJANGO RELATED STUFF ONLY!

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e-)^!t4%*e$63q&@q5pjk4479+d7(ttg-=9#@cfr26$==ud75x'

APPEND_SLASH = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_injector',

    'infrastructure.db.account'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_injector.apps.inject_request_middleware'
]

INJECTOR_MODULES = [
    'integration.extensions.di.DIModule'
]

ROOT_URLCONF = 'integration.server.urls'

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
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

WSGI_APPLICATION = 'integration.server.wsgi.application'

AUTH_USER_MODEL = 'account.AppUser'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3'
  }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'integration.contrib.auth.authenticators.access.CookieBasedAccessJWTAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'integration.contrib.auth.permissions.IsAuthenticated'
    ],
    'EXCEPTION_HANDLER': 'integration.contrib.api.exception_handler.response'
}

JWT_COOKIE_AUTH = {
    'ACCESS_TOKEN_KEY': 'access-token',
    'REFRESH_TOKEN_KEY': 'refresh-token',
    'HTTP_ONLY': conf.jwt_auth.http_only_cookie,
    'SECURE_ONLY': False,
    'SAME_SITE': 'Strict' if conf.jwt_auth.strict_origin_cookie else 'None'
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    }
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'