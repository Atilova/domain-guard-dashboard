# from typing import Optional, Generic, Tuple

from dataclasses import dataclass

from domain.ValueObjects.auth import (
    AppUserId,
    AppUserEmail,
    AppUserUsername,
    AppUserFirstName,
)


@dataclass
class AppUser:
    """AppUser"""

    id: AppUserId
    email: AppUserEmail
    username: AppUserUsername
    first_name: AppUserFirstName

    def __str__(self):
        return f'<User id={self.id.raw()} username={self.username.raw()} />'