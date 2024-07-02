from application.codes.auth import AuthCodes
from application.adapters.Interactor import Interactor
from application.adapters.auth.IAuthActionService import IAuthActionService
from application.Dto.auth.logout import AuthLogoutInputDTO, AuthLogoutOutputDTO

from domain.ValueObjects.jwt import JwtToken


class AuthLogoutUseCase(Interactor[AuthLogoutInputDTO, AuthLogoutOutputDTO]):
    """AuthLogoutUseCase"""

    def __init__(self, *, auth_service: IAuthActionService):
        self.__auth_service = auth_service

    def __call__(self, data: AuthLogoutInputDTO) -> AuthLogoutOutputDTO:
        refresh = JwtToken(data.refresh_token)
        self.__auth_service.logout(refresh)

        return AuthLogoutOutputDTO(
            code=AuthCodes.LOGOUT_FULFILLED
        )
