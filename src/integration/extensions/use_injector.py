from django.apps import apps

from injector import Injector

from typing import Callable, Any


_django_injector_app = apps.get_app_config('django_injector')
_injector: Injector = _django_injector_app.injector

def use_injector(function: Callable[[Any], Any]):
    """use_injector"""

    return lambda: _injector.get(function)
