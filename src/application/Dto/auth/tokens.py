from datetime import datetime

from typing import NamedTuple


class Token(NamedTuple):
    """Token"""

    token: str
    expires_at: datetime


class AuthTokens(NamedTuple):
    """AuthTokens"""

    access: Token
    refresh: Token