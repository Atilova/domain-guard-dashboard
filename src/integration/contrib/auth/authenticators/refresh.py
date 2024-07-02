from injector import inject

from django.http.request import HttpRequest

from .base import BaseCookieBasedJWTAuthentication

from integration.extensions.use_injector import use_injector
from integration.adapters.accounts.IAccountInteractor import IAccountInteractor
from integration.contrib.auth.cookies import get_refresh_token_cookie
from integration.exceptions.auth import RefreshNotAuthenticated, RefreshAuthenticationFailed

from application.codes.auth import AuthCodes
from application.Dto.auth.authenticate import AuthRefreshAuthenticateUserInputDTO


@use_injector
class CookieBasedRefreshJWTAuthentication(BaseCookieBasedJWTAuthentication):
    """CookieBasedRefreshJWTAuthentication"""

    NotAuthenticatedException = RefreshNotAuthenticated
    AuthenticationFailedException = RefreshAuthenticationFailed

    @inject
    def __init__(self, ioc: IAccountInteractor):
        self.__ioc = ioc

    def authentication_method(self):
        return self.__ioc.authenticate_refresh()

    def get_input_dto(self, request: HttpRequest):
        return AuthRefreshAuthenticateUserInputDTO(
            refresh_token=get_refresh_token_cookie(request)
        )

    @property
    def user_authenticated_code(self):
        return AuthCodes.USER_AUTHENTICATED_FROM_REFRESH

    @property
    def token_unset_code(self):
        return AuthCodes.REFRESH_TOKEN_UNSET

    @property
    def token_invalid_signature_code(self):
        return AuthCodes.REFRESH_TOKEN_INVALID_SIGNATURE
