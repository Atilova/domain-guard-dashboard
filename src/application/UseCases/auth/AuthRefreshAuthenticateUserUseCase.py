from application.codes.auth import AuthCodes
from application.adapters.Interactor import Interactor
from application.adapters.auth.IAuthActionService import IAuthActionService
from application.Dto.auth.user import AuthenticatedUserDTO
from application.Dto.auth.authenticate import AuthRefreshAuthenticateUserInputDTO, AuthAuthenticateUserOutputDTO

from domain.ValueObjects.jwt import JwtToken


class AuthRefreshAuthenticateUserUseCase(Interactor[AuthRefreshAuthenticateUserInputDTO, AuthAuthenticateUserOutputDTO]):
    """AuthRefreshAuthenticateUserUseCase"""

    def __init__(self, *, auth_service: IAuthActionService):
        self.__auth_service = auth_service

    def __call__(self, data: AuthRefreshAuthenticateUserInputDTO) -> AuthAuthenticateUserOutputDTO:
        try:
            refresh = JwtToken(data.refresh_token)
        except ValueError:
            return AuthAuthenticateUserOutputDTO(code=AuthCodes.REFRESH_TOKEN_UNSET)

        user = self.__auth_service.user_from_refresh(refresh)
        if not user: return AuthAuthenticateUserOutputDTO(code=AuthCodes.REFRESH_TOKEN_INVALID_SIGNATURE)
       
        return AuthAuthenticateUserOutputDTO(
            code=AuthCodes.USER_AUTHENTICATED_FROM_REFRESH,
            user=AuthenticatedUserDTO.from_app_user(user)
        )
