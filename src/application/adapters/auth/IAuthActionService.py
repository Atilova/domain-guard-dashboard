from typing import Optional, Protocol

from domain.Entities.auth import AppUser
from domain.Entities.jwt import JwtTokenHolder, JwtTokenPair
from domain.ValueObjects.auth import AppUserUsername, AppUserPassword
from domain.ValueObjects.jwt import JwtToken


class IAuthActionService(Protocol):
    """IAuthActionService"""

    def authenticate(self, username: AppUserUsername, password: AppUserPassword) -> Optional[AppUser]:
        pass

    def login(self, user: AppUser) -> JwtTokenPair:
        pass

    def renew_access(self, token: JwtToken) -> Optional[JwtTokenHolder]:
        pass

    def logout(self, user: AppUser) -> None:
        pass

    def user_from_access(self, token: JwtToken):
        pass

    def user_from_refresh(self, token: JwtToken):
        pass