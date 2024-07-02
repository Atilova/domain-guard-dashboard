from domain.Enums.jwt import JwtTokenType
from domain.Entities.jwt import JwtTokenPair, JwtTokenSignature
from domain.ValueObjects.app import AppDateTime
from domain.ValueObjects.auth import AppUserId
from domain.ValueObjects.jwt import JwtToken


class JwtTokenService:
    """JwtTokenService"""

    def new_pair(self, *,
        access: JwtToken,
        access_signature: JwtTokenSignature,
        refresh: JwtToken,
        refresh_signature: JwtTokenSignature
    ) -> JwtTokenPair:
        return JwtTokenPair(
            access=access,
            access_signature=access_signature,
            refresh=refresh,
            refresh_signature=refresh_signature
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