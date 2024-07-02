from django.utils.timezone import make_aware

from domain.Entities.auth import AppUser
from domain.Entities.jwt import JwtTokenSignature
from domain.ValueObjects.auth import (
    AppUserId
)
from domain.ValueObjects.jwt import JwtToken

from infrastructure.db.account.models import (
    AppUser as AppUserModel,
    RefreshToken as RefreshTokenModel
)
from infrastructure.adapters.auth.IAuthUserService import IAuthUserService
from infrastructure.db.account.map_django_to_app_user import map_django_to_app_user


class AuthUserRepository:
    """AuthUserRepository"""

    def __init__(self, service: IAuthUserService):
        self.__service = service

    def from_id(self, user_id: AppUserId):
        return AppUserModel.objects.get(id=user_id.raw())

    def from_signature(self, signature: JwtTokenSignature) -> AppUser:
        django_user = self.from_id(signature.user_id)
        return map_django_to_app_user(self.__service, django_user)

    def link_token(self,
        user: AppUser,
        refresh_token: JwtToken,
        signature: JwtTokenSignature
    ):
        mock_user = AppUserModel(id=user.id.raw())
        RefreshTokenModel.objects.create(
            user=mock_user,
            token=refresh_token.raw(),
            issued_at=make_aware(signature.iat.raw()),
            expires_at=make_aware(signature.exp.raw())
        )

    def token_exists(self, token: JwtToken) -> bool:
        django_token = self._get_token(token)
        return django_token is not None

    def invalidate_token(self, token: JwtToken):
        django_token = self._get_token(token)
        if django_token is None: return

        django_token.delete()

    def _get_token(self, token: JwtToken):
        try:
            django_token = RefreshTokenModel.objects.get(token=token.raw())
        except RefreshTokenModel.DoesNotExist:
            return None
        return django_token
