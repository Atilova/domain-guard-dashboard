from typing import Protocol

from domain.ValueObjects.jwt import JwtToken


class IJwtAuthTokenRepository(Protocol):
    """IJwtAuthTokenRepository"""

    def blacklist(self, token: JwtToken):
        pass