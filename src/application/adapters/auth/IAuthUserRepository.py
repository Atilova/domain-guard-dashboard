from typing import Protocol

from domain.Entities.auth import AppUser
from domain.Entities.jwt import JwtTokenHolder, JwtTokenSignature
from domain.ValueObjects.jwt import JwtToken


class IAuthUserRepository(Protocol):
    """IAuthUserRepository"""

    def from_signature(self, signature: JwtTokenSignature) -> AppUser:
        pass

    def link_token(self, user: AppUser, token_holder: JwtTokenHolder) -> None:
        pass

    def token_exists(self, token: JwtToken) -> bool:
        pass

    def invalidate_token(self, token: JwtToken) -> None:
        pass