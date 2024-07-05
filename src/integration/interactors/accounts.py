from config import conf

from redis import Redis
from contextlib import contextmanager

from typing import Iterator

from application.UseCases.auth.AuthLoginUseCase import AuthLoginUseCase
from application.UseCases.auth.AuthLogoutUseCase import AuthLogoutUseCase
from application.UseCases.auth.AuthRefreshTokenUseCase import AuthRefreshTokenUseCase
from application.UseCases.auth.AuthAuthenticateUserUseCase import AuthAuthenticateUserUseCase
from application.UseCases.auth.AuthRefreshAuthenticateUserUseCase import AuthRefreshAuthenticateUserUseCase

from domain.Services.auth import AuthUserService
from domain.Services.jwt import JwtTokenService

from infrastructure.services.auth import AuthActionService
from infrastructure.services.jwt import JwtAuthTokenService
from infrastructure.redis.storages.record import RedisRecordStorage
from infrastructure.repositories.auth.user import AuthUserRepository


class AccountInteractorFactory:
    """AccountInteractorFactory"""

    def __init__(self, redis_client: Redis):
        self.__redis_client = redis_client
        self.__jwt_auth_token_service = JwtAuthTokenService(
            config=conf.jwt_auth,
            service=JwtTokenService()
        )
        self.__auth_user_repository = AuthUserRepository(
            service=AuthUserService()
        )
        self.__auth_action_service = AuthActionService(
            service=AuthUserService(),
            record_storage=RedisRecordStorage(
                prefix='signup',
                client=self.__redis_client,
                key='email'
            ),
            jwt_service=self.__jwt_auth_token_service,
            repository=self.__auth_user_repository
        )

    @contextmanager
    def authenticate(self) -> Iterator[AuthAuthenticateUserUseCase]:
        yield AuthAuthenticateUserUseCase(
            auth_service=self.__auth_action_service
        )

    @contextmanager
    def authenticate_refresh(self) -> Iterator[AuthRefreshAuthenticateUserUseCase]:
        yield AuthRefreshAuthenticateUserUseCase(
           auth_service=self.__auth_action_service
        )

    @contextmanager
    def login(self) -> Iterator[AuthLoginUseCase]:
        yield AuthLoginUseCase(
           auth_service=self.__auth_action_service
        )

    @contextmanager
    def refresh(self) -> Iterator[AuthRefreshTokenUseCase]:
        yield AuthRefreshTokenUseCase(
            auth_service=self.__auth_action_service
        )

    @contextmanager
    def logout(self) -> Iterator[AuthLogoutUseCase]:
        yield AuthLogoutUseCase(
            auth_service=self.__auth_action_service
        )