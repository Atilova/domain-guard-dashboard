from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    'domain.com'
]

REST_FRAMEWORK |= {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ]
}

JWT_COOKIE_AUTH['SECURE_ONLY'] = True
