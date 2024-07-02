from django.http.request import HttpRequest

from rest_framework.authentication import BaseAuthentication

from integration.exceptions.auth import NotAuthenticated, AuthenticationFailed


class BaseCookieBasedJWTAuthentication(BaseAuthentication):
    """BaseCookieBasedJWTAuthentication"""

    NotAuthenticatedException = NotAuthenticated
    AuthenticationFailedException = AuthenticationFailed

    def authenticate(self, request: HttpRequest):
        with self.authentication_method() as authenticate:
            dto = authenticate(self.get_input_dto(request))

        code = dto.code
        if code == self.user_authenticated_code:
            return dto.user, None

        if code == self.token_unset_code:
            raise self.NotAuthenticatedException(code)

        raise self.AuthenticationFailedException(code)

    def authentication_method(self):
        raise NotImplementedError

    def get_input_dto(self, request: HttpRequest):
        raise NotImplementedError

    @property
    def user_authenticated_code(self):
        raise NotImplementedError
    
    @property
    def token_unset_code(self):
        raise NotImplementedError
    
    @property
    def token_invalid_signature_code(self):
        raise NotImplementedError
    