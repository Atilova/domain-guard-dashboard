from datetime import datetime

from dataclasses import dataclass

from domain.Enums.jwt import JwtTokenType
from domain.ValueObjects.app import AppDateTime
from domain.ValueObjects.auth import AppUserId
from domain.ValueObjects.jwt import JwtToken


@dataclass
class JwtTokenSignature:
    """JwtTokenSignature"""

    user_id: AppUserId
    exp: AppDateTime
    iat: AppDateTime
    type: JwtTokenType

    def to_dict(self):
        return {
            'exp': self.exp.raw().timestamp(),
            'iat': self.iat.raw().timestamp(),
            'user_id': self.user_id.raw(),
            'type': self.type.value
        }


@dataclass
class JwtTokenPair:
    """JwtTokenPair"""

    access: JwtToken
    access_signature: JwtTokenSignature
    refresh: JwtToken
    refresh_signature: JwtTokenSignature