from application.codes.auth import AuthCodes
from application.adapters.Interactor import Interactor
from application.adapters.auth.IAuthActionService import IAuthActionService
from application.Dto.auth.user import AuthenticatedUserDTO
from application.Dto.auth.authenticate import AuthAuthenticateUserInputDTO, AuthAuthenticateUserOutputDTO

from domain.ValueObjects.jwt import JwtToken


class AuthAuthenticateUserUseCase(Interactor[AuthAuthenticateUserInputDTO, AuthAuthenticateUserOutputDTO]):
    """AuthAuthenticateUserUseCase"""

    def __init__(self, *, auth_service: IAuthActionService):
        self.__auth_service = auth_service

    def __call__(self, data: AuthAuthenticateUserInputDTO) -> AuthAuthenticateUserOutputDTO:
        try:
            access = JwtToken(data.access_token)
        except ValueError:
            return AuthAuthenticateUserOutputDTO(code=AuthCodes.ACCESS_TOKEN_UNSET)

        user = self.__auth_service.user_from_access(access)
        if user is None: return AuthAuthenticateUserOutputDTO(code=AuthCodes.ACCESS_TOKEN_INVALID_SIGNATURE)

        return AuthAuthenticateUserOutputDTO(
            code=AuthCodes.USER_AUTHENTICATED,
            user=AuthenticatedUserDTO.from_app_user(user)
        )
