from django.utils.translation import gettext_lazy as _

from rest_framework import status

from .base import AppAPIException


class NotAuthenticated(AppAPIException):
    """NotAuthenticated"""

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Access token was not provided.')


class AuthenticationFailed(AppAPIException):
    """AuthenticationFailed"""

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Access token invalid signature.')


class RefreshNotAuthenticated(NotAuthenticated):
    """RefreshNotAuthenticated"""

    default_detail = _('Refresh token was not provided.')


class RefreshAuthenticationFailed(AuthenticationFailed):
    """RefreshNotAuthenticated"""

    default_detail = _('Refresh token invalid signature.')
