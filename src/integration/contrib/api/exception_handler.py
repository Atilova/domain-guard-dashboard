from rest_framework import views

from integration.contrib.auth.cookies import delete_auth_cookies
from integration.exceptions.base import AppAPIException
from integration.exceptions.auth import RefreshNotAuthenticated, RefreshAuthenticationFailed

def _get_message_from_code(code: int, detail: str):
    """_get_message_from_code"""

    # Todo: implement.
    return detail

def response(exc, context):
    """response"""

    response = views.exception_handler(exc, context)

    if isinstance(exc, (RefreshNotAuthenticated, RefreshAuthenticationFailed)):
        delete_auth_cookies(response)

    if isinstance(exc, AppAPIException):
        response.data = {
            'code': exc.code,
            'detail': _get_message_from_code(exc.code, exc.detail) # Detail describing exc.code from application.codes
        }

    return response