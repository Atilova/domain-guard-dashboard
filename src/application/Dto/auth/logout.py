from dataclasses import dataclass

from .user import AuthenticatedUserDTO

from application.codes.auth import AuthCodes


@dataclass(frozen=True)
class AuthLogoutInputDTO:
    """AuthLogoutInputDTO"""

    refresh_token: str


@dataclass(frozen=True)
class AuthLogoutOutputDTO:
    """AuthLogoutOutputDTO"""

    code: AuthCodes