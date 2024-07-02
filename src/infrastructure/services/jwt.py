import jwt

from datetime import datetime, timedelta

from typing import Optional

from domain.Enums.jwt import JwtTokenType
from domain.Entities.auth import AppUser
from domain.Entities.jwt import JwtTokenPair, JwtTokenSignature
from domain.ValueObjects.app import AppDateTime
from domain.ValueObjects.auth import AppUserId
from domain.ValueObjects.jwt import JwtToken

from infrastructure.config import JwtAuthConfig
from infrastructure.adapters.jwt.IJwtTokenService import IJwtTokenService


def _make_generator(
    service: IJwtTokenService, *,
    token_type: JwtTokenType,
    expiration: timedelta,
    secret: str,
    algorithm: str='HS256'
):
    """_make_generator"""

    def new_token(user_id: AppUserId):
        now = datetime.now()
        signature = service.new_signature(
            user_id=user_id,
            exp=AppDateTime(now + expiration),
            iat=AppDateTime(now),
            type=token_type
        )

        token = jwt.encode(signature.to_dict(), secret, algorithm)
        return token, signature

    return new_token

def _make_decoder(
    service: IJwtTokenService, *,
    secret: str,
    algorithm: str='HS256'
):
    """_make_decoder"""

    def decode(token: JwtToken) -> Optional[JwtTokenSignature]:
        try:
            payload = jwt.decode(token.raw(), secret, algorithm)
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
            return None

        return service.new_signature(
            user_id=AppUserId(payload['user_id']),
            exp=_init_datetime(payload['exp']),
            iat=_init_datetime(payload['iat']),
            type=JwtTokenType.from_str(payload['type'])
        )

    return decode

def _init_datetime(timestamp: float) -> AppDateTime:
    return AppDateTime(
        datetime.fromtimestamp(timestamp)
    )


class JwtAuthTokenService:
    """JwtAuthTokenService"""

    def __init__(self, *,
        config: JwtAuthConfig,
        service: IJwtTokenService,
    ):
        self.__config = config
        self.__service = service
        self.__new_access = _make_generator(
            service=self.__service,
            token_type=JwtTokenType.APP_ACCESS,
            expiration=self.__config.access_token_expiration_delta,
            secret=self.__config.secret,
            algorithm=self.__config.algorithm
        )
        self.__new_refresh = _make_generator(
            service=self.__service,
            token_type=JwtTokenType.APP_REFRESH,
            expiration=self.__config.refresh_token_expiration_delta,
            secret=self.__config.secret,
            algorithm=self.__config.algorithm
        )
        self.__decode = _make_decoder(
            service=self.__service,
            secret=self.__config.secret,
            algorithm=self.__config.algorithm
        )

    def obtain_pair(self, user: AppUser) -> JwtTokenPair:
        user_id = user.id

        access_token, access_signature = self.__new_access(user_id)
        refresh_token, refresh_signature = self.__new_refresh(user_id)

        return self.__service.new_pair(
            access=JwtToken(access_token),
            access_signature=access_signature,
            refresh=JwtToken(refresh_token),
            refresh_signature=refresh_signature
        )

    def decode_token(self, token: JwtToken, token_type: JwtTokenType) -> Optional[JwtTokenSignature]:
        signature = self.__decode(token)
        if signature is None or signature.type is not token_type: return None
        return signature

    def decode_access(self, token: JwtToken) -> Optional[JwtTokenSignature]:
        return self.decode_token(token, JwtTokenType.APP_ACCESS)

    def decode_refresh(self, token: JwtToken) -> Optional[JwtTokenSignature]:
        return self.decode_token(token, JwtTokenType.APP_REFRESH)
