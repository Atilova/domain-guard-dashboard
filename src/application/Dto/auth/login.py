from typing import Optional
from dataclasses import dataclass

from .tokens import AuthTokens

from application.codes.auth import AuthCodes


@dataclass(frozen=True)
class AuthLoginInputDTO:
    """AuthLoginInputDTO"""

    username: str
    password: str
    refresh_token: str


@dataclass(frozen=True)
class AuthLoginOutputDTO:
    """AuthLoginOutputDTO"""

    code: AuthCodes
    tokens: Optional[AuthTokens] = None
