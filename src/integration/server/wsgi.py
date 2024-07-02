import os

from django.core.wsgi import get_wsgi_application

from config import conf

os.environ.setdefault('DJANGO_SETTINGS_MODULE', conf.django.settings_module)

application = get_wsgi_application()
