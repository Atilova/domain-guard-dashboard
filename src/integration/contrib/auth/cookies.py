from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response

from application.Dto.auth.tokens import AuthTokens, Token


cookie_config = settings.JWT_COOKIE_AUTH

def get_access_token_cookie(request: Request):
    return request.COOKIES.get(cookie_config['ACCESS_TOKEN_KEY'])

def get_refresh_token_cookie(request: Request):
    return request.COOKIES.get(cookie_config['REFRESH_TOKEN_KEY'])

def set_access_token_cookie(response: Response, access: Token):
    """set_access_token_cookie"""

    response.set_cookie(
        key=cookie_config['ACCESS_TOKEN_KEY'],
        value=access.token,
        expires=access.expires_at,
        httponly=cookie_config['HTTP_ONLY'],
        secure=cookie_config['SECURE_ONLY'],
        samesite=cookie_config['SAME_SITE']
    )
    return response

def set_refresh_token_cookie(response: Response, refresh: Token):
    """set_refresh_token_cookie"""

    response.set_cookie(
        key=cookie_config['REFRESH_TOKEN_KEY'],
        value=refresh.token,
        expires=refresh.expires_at,
        httponly=cookie_config['HTTP_ONLY'],
        secure=cookie_config['SECURE_ONLY'],
        samesite=cookie_config['SAME_SITE']
    )
    return response

def set_auth_cookies(response: Response, token: AuthTokens):
    """set_auth_cookies"""

    response = set_access_token_cookie(response, token.access)
    return set_refresh_token_cookie(response, token.refresh)

def delete_auth_cookies(response: Response):
    """delete_auth_cookies"""

    response.delete_cookie(cookie_config['ACCESS_TOKEN_KEY'])
    response.delete_cookie(cookie_config['REFRESH_TOKEN_KEY'])

    return response
