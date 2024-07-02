from dataclasses import dataclass

from domain.Entities.auth import AppUser


@dataclass(frozen=True)
class AuthenticatedUserDTO:
    """AuthenticatedAppUser"""

    id: int
    email: str
    username: str
    first_name: str

    @classmethod
    def from_app_user(cls, user: AppUser):
        return cls(
            id=user.id.raw(),
            email=user.email.raw(),
            username=user.username.raw(),
            first_name=user.first_name.raw(),
        )

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username
