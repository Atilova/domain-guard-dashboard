from application.codes.auth import AuthCodes
from application.adapters.Interactor import Interactor
from application.adapters.auth.IAuthActionService import IAuthActionService
from application.Dto.auth.tokens import Token
from application.Dto.auth.refresh import AuthRefreshTokenInputDTO, AuthRefreshTokenOutputDTO

from domain.ValueObjects.jwt import JwtToken


class AuthRefreshTokenUseCase(Interactor[AuthRefreshTokenInputDTO, AuthRefreshTokenOutputDTO]):
    """AuthRefreshAuthenticateUserUseCase"""

    def __init__(self, *, auth_service: IAuthActionService):
        self.__auth_service = auth_service

    def __call__(self, data: AuthRefreshTokenInputDTO) -> AuthRefreshTokenOutputDTO:
        try:
            refresh = JwtToken(data.refresh_token)
        except ValueError:
            return AuthRefreshTokenOutputDTO(code=AuthCodes.REFRESH_TOKEN_UNSET)

        new_access = self.__auth_service.renew_access(refresh)
        if not new_access: return AuthRefreshTokenOutputDTO(code=AuthCodes.REFRESH_TOKEN_INVALID_SIGNATURE)

        return AuthRefreshTokenOutputDTO(
            code=AuthCodes.ACCESS_TOKEN_ISSUED,
            access=Token(
                token=new_access.token.raw(),
                expires_at=new_access.signature.exp.raw()
            )
        )
