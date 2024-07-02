from application.codes.auth import AuthCodes
from application.adapters.Interactor import Interactor
from application.adapters.auth.IAuthActionService import IAuthActionService
from application.Dto.auth.login import AuthLoginInputDTO, AuthLoginOutputDTO
from application.Dto.auth.tokens import AuthTokens, Token

from domain.ValueObjects.auth import AppUserEmail, AppUserPassword
from domain.ValueObjects.jwt import JwtToken


class AuthLoginUseCase(Interactor[AuthLoginInputDTO, AuthLoginOutputDTO]):
    """AuthLoginUseCase"""

    def __init__(self, *, auth_service: IAuthActionService):
        self.__auth_service = auth_service

    def __call__(self, data: AuthLoginInputDTO) -> AuthLoginOutputDTO:
        try:
            refresh_token = JwtToken(data.refresh_token)
            user = self.__auth_service.user_from_refresh(refresh_token)
            if user is not None: return AuthLoginOutputDTO(code=AuthCodes.USER_ALREADY_AUTHENTICATED)
        except ValueError: pass

        try:
            username, password = AppUserEmail(data.username), AppUserPassword(data.password)
        except ValueError:
            return AuthLoginOutputDTO(code=AuthCodes.CREDENTIALS_UNSET)

        user = self.__auth_service.authenticate(username, password)
        if user is None: return AuthLoginOutputDTO(code=AuthCodes.WRONG_CREDENTIALS)

        token_pair = self.__auth_service.login(user)
        return AuthLoginOutputDTO(
            code=AuthCodes.TOKEN_PAIR_ISSUED,
            tokens=AuthTokens(
                access=Token(
                    token=token_pair.access.raw(),
                    expires_at=token_pair.access_signature.exp.raw()
                ),
                refresh=Token(
                    token=token_pair.refresh.raw(),
                    expires_at=token_pair.refresh_signature.exp.raw()
                )
            )
        )
