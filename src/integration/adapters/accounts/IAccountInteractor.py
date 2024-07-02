from typing import Protocol, ContextManager

from application.UseCases.auth.AuthLoginUseCase import AuthLoginUseCase
from application.UseCases.auth.AuthLogoutUseCase import AuthLogoutUseCase
from application.UseCases.auth.AuthAuthenticateUserUseCase import AuthAuthenticateUserUseCase
from application.UseCases.auth.AuthRefreshAuthenticateUserUseCase import AuthRefreshAuthenticateUserUseCase


class IAccountInteractor(Protocol):
    """IAccountInteractor"""

    def authenticate(self) -> ContextManager[AuthAuthenticateUserUseCase]:
        pass

    def authenticate_refresh(self) -> ContextManager[AuthRefreshAuthenticateUserUseCase]:
        pass

    def login(self) -> ContextManager[AuthLoginUseCase]:
        pass

    def logout(self) -> ContextManager[AuthLogoutUseCase]:
        pass
