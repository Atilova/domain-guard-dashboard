from typing import Protocol

from domain.Enums.jwt import JwtTokenType
from domain.Entities.jwt import JwtTokenPair, JwtTokenSignature
from domain.ValueObjects.app import AppDateTime
from domain.ValueObjects.auth import AppUserId
from domain.ValueObjects.jwt import JwtToken


class IJwtTokenService(Protocol):
    """IJwtTokenService"""

    def new_pair(self, *,
        access: JwtToken,
        access_signature: JwtTokenSignature,
        refresh: JwtToken,
        refresh_signature: JwtTokenSignature
    ) -> JwtTokenPair:
        pass

    def new_signature(self, *,
        user_id: AppUserId,
        exp: AppDateTime,
        iat: AppDateTime,
        type: JwtTokenType
    ) -> JwtTokenSignature:
        pass