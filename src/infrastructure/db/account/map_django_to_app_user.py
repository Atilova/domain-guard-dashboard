from .models import AppUser as AppUserModel

from domain.Entities.auth import AppUser
from domain.ValueObjects.auth import (
    AppUserId,
    AppUserEmail,
    AppUserUsername,
    AppUserFirstName
)

from infrastructure.adapters.auth.IAuthUserService import IAuthUserService


def map_django_to_app_user(service: IAuthUserService, django_user: AppUserModel) -> AppUser:
    """map_django_to_app_user"""

    return service.new_user(
        id=AppUserId(django_user.id),
        email=AppUserEmail(django_user.email),
        username=AppUserUsername(django_user.username),
        first_name=AppUserFirstName(django_user.first_name)
    )
