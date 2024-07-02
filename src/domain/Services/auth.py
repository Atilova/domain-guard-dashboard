from domain.Entities.auth import AppUser
from domain.ValueObjects.auth import (
    AppUserId,
    AppUserEmail,
    AppUserUsername,
    AppUserFirstName
)


class AuthUserService:
    """AuthUserService"""

    def new_user(self, *,
        id: AppUserId,
        email: AppUserEmail,
        username: AppUserUsername,
        first_name: AppUserFirstName
    ) -> AppUser:
        return AppUser(
            id=id,
            email=email,
            username=username,
            first_name=first_name
        )