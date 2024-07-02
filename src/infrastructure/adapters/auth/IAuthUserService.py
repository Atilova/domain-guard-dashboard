from typing import Protocol

from domain.Entities.auth import AppUser
from domain.ValueObjects.auth import (
    AppUserId,
    AppUserEmail,
    AppUserUsername,
    AppUserFirstName
)


class IAuthUserService(Protocol):
    """IAuthUserService"""

    def new_user(self, *,
        id: AppUserId,
        email: AppUserEmail,
        username: AppUserUsername,
        first_name: AppUserFirstName
    ) -> AppUser:
        pass