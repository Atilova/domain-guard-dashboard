from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException

from typing import Optional


class AppAPIException(APIException):
    """AppAPIException"""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('A server error occurred.')

    def __init__(self, code: int, detail: Optional[str]=None):
        self.__code = code
        self.__detail = detail or self.default_detail

    def __str__(self):
        return f'<AppAPIException code={self.__code} detail={self.__detail} />'

    @property
    def code(self):
        return self.__code

    @property
    def detail(self):
        return self.__detail
