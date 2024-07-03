from django.contrib.auth import authenticate

from typing import Optional, Callable

from domain.Entities.auth import AppUser
from domain.Entities.jwt import (
    JwtTokenPair,
    JwtTokenHolder,
    JwtTokenSignature
)
from domain.ValueObjects.auth import (
    AppUserUsername,
    AppUserPassword
)
from domain.ValueObjects.jwt import JwtToken

from infrastructure.adapters.auth.IAuthUserService import IAuthUserService
from infrastructure.adapters.auth.IAuthUserRepository import IAuthUserRepository
from infrastructure.adapters.jwt.IJwtAuthTokenService import IJwtAuthTokenService
from infrastructure.db.account.map_django_to_app_user import map_django_to_app_user


class AuthActionService:
    """AuthActionService"""

    def __init__(self, *,
        service: IAuthUserService,
        jwt_service: IJwtAuthTokenService,
        repository: IAuthUserRepository
    ):
        self.__service = service
        self.__jwt_service = jwt_service
        self.__repository = repository

    def authenticate(self, username: AppUserUsername, password: AppUserPassword) -> Optional[AppUser]:
        django_user = authenticate(username=username.raw(), password=password.raw())
        if django_user is None: return None

        return map_django_to_app_user(self.__service, django_user)

    def login(self, user: AppUser) -> JwtTokenPair:
        token_pair = self.__jwt_service.obtain_pair(user)
        self.__repository.link_token(user, token_pair.refresh)

        return token_pair

    def renew_access(self, token: JwtToken) -> Optional[JwtTokenHolder]:
        user = self.user_from_refresh(token)
        if user is None: return None

        return self.__jwt_service.obtain_access(user)

    def logout(self, token: JwtToken):
        self.__repository.invalidate_token(token)

    def user_from_access(self, token: JwtToken) -> Optional[AppUser]:
       return self._user_from_token(token, self.__jwt_service.decode_access)

    def user_from_refresh(self, token: JwtToken) -> Optional[AppUser]:
        is_active = self.__repository.token_exists(token)
        if not is_active: return None

        return self._user_from_token(token, self.__jwt_service.decode_refresh)

    def _user_from_token(self,
        token: JwtToken,
        decoder: Callable[[JwtToken], Optional[JwtTokenSignature]]
    ) -> Optional[AppUser]:
        signature = decoder(token)
        if not signature: return None

        return self.__repository.from_signature(signature)
