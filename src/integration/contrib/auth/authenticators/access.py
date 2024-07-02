from injector import inject

from django.http.request import HttpRequest

from .base import BaseCookieBasedJWTAuthentication

from integration.extensions.use_injector import use_injector
from integration.adapters.accounts.IAccountInteractor import IAccountInteractor
from integration.contrib.auth.cookies import get_access_token_cookie
from integration.exceptions.auth import NotAuthenticated, AuthenticationFailed

from application.codes.auth import AuthCodes
from application.Dto.auth.authenticate import AuthAuthenticateUserInputDTO

@use_injector
class CookieBasedAccessJWTAuthentication(BaseCookieBasedJWTAuthentication):
    """CookieBasedAccessJWTAuthentication"""

    NotAuthenticatedException = NotAuthenticated
    AuthenticationFailedException = AuthenticationFailed

    @inject
    def __init__(self, ioc: IAccountInteractor):
        self.__ioc = ioc

    def authentication_method(self):
        return self.__ioc.authenticate()

    def get_input_dto(self, request: HttpRequest):
        return AuthAuthenticateUserInputDTO(
            access_token=get_access_token_cookie(request)
        )

    @property
    def user_authenticated_code(self):
        return AuthCodes.USER_AUTHENTICATED

    @property
    def token_unset_code(self):
        return AuthCodes.ACCESS_TOKEN_UNSET

    @property
    def token_invalid_signature_code(self):
        return AuthCodes.ACCESS_TOKEN_INVALID_SIGNATURE
