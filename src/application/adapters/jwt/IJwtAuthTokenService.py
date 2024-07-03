from typing import Optional, Protocol

from domain.Entities.auth import AppUser
from domain.Entities.jwt import (
    JwtTokenPair,
    JwtTokenHolder,
    JwtTokenSignature
)
from domain.ValueObjects.jwt import JwtToken


class IJwtAuthTokenService(Protocol):
    """IJwtAuthTokenService"""

    def obtain_access(self, user: AppUser) -> JwtTokenHolder:
        pass

    def obtain_refresh(self, user: AppUser) -> JwtTokenHolder:
        pass

    def obtain_pair(self, user: AppUser) -> JwtTokenPair:
        pass

    def decode_access(self, token: JwtToken) -> Optional[JwtTokenSignature]:
        pass

    def decode_refresh(self, token: JwtToken) -> Optional[JwtTokenSignature]:
        pass
