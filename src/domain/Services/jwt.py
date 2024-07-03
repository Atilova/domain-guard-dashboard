from domain.Enums.jwt import JwtTokenType
from domain.Entities.jwt import (
    JwtTokenPair,
    JwtTokenHolder,
    JwtTokenSignature
)
from domain.ValueObjects.app import AppDateTime
from domain.ValueObjects.auth import AppUserId
from domain.ValueObjects.jwt import JwtToken


class JwtTokenService:
    """JwtTokenService"""

    def new_token(self, *,
        token: JwtToken,
        signature: JwtTokenSignature
    ) -> JwtTokenHolder:
        return JwtTokenHolder(
            token=token,
            signature=signature
        )

    def new_pair(self, *,
        access: JwtTokenHolder,
        refresh: JwtTokenHolder
    ) -> JwtTokenPair:
        return JwtTokenPair(
            access=access,
            refresh=refresh
        )

    def new_signature(self, *,
        user_id: AppUserId,
        exp: AppDateTime,
        iat: AppDateTime,
        type: JwtTokenType
    ) -> JwtTokenSignature:
        return JwtTokenSignature(
            user_id=user_id,
            exp=exp,
            iat=iat,
            type =type
        )