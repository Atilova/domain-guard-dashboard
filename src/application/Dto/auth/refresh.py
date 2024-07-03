from dataclasses import dataclass

from .tokens import Token

from application.codes.auth import AuthCodes


@dataclass(frozen=True)
class AuthRefreshTokenInputDTO:
    """AuthRefreshTokenInputDTO"""

    refresh_token: str


@dataclass(frozen=True)
class AuthRefreshTokenOutputDTO:
    """AuthRefreshTokenOutputDTO"""

    code: AuthCodes
    access: Token