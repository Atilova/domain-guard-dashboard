from typing import Optional
from dataclasses import dataclass

from .user import AuthenticatedUserDTO

from application.codes.auth import AuthCodes


@dataclass(frozen=True)
class AuthAuthenticateUserInputDTO:
    """AuthAuthenticateUserInputDTO"""

    access_token: str
   

@dataclass(frozen=True)
class AuthRefreshAuthenticateUserInputDTO:
    """AuthRefreshAuthenticateUserInputDTO"""

    refresh_token: str


@dataclass(frozen=True)
class AuthAuthenticateUserOutputDTO:
    """AuthAuthenticateUserOutputDTO"""

    code: AuthCodes
    user: Optional[AuthenticatedUserDTO] = None