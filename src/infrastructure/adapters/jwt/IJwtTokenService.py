from typing import Protocol

from domain.Enums.jwt import JwtTokenType
from domain.Entities.jwt import (
    JwtTokenPair,
    JwtTokenHolder,
    JwtTokenSignature
)
from domain.ValueObjects.app import AppDateTime
from domain.ValueObjects.auth import AppUserId
from domain.ValueObjects.jwt import JwtToken


class IJwtTokenService(Protocol):
    """IJwtTokenService"""

    def new_token(self, *,
            token: JwtToken,
            signature: JwtTokenSignature
        ) -> JwtTokenHolder:
        pass

    def new_pair(self, *,
        access_signature: JwtTokenHolder,
        refresh_signature: JwtTokenHolder
    ) -> JwtTokenPair:
        pass

    def new_signature(self, *,
        user_id: AppUserId,
        exp: AppDateTime,
        iat: AppDateTime,
        type: JwtTokenType
    ) -> JwtTokenSignature:
        pass