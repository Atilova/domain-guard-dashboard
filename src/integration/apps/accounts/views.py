from injector import inject

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import LoginSerializer

from integration.adapters.accounts.IAccountInteractor import IAccountInteractor
from integration.contrib.auth.cookies import (
    set_auth_cookies,
    delete_auth_cookies,
    set_access_token_cookie,
    get_refresh_token_cookie
)
from integration.contrib.auth.authenticators.refresh import CookieBasedRefreshJWTAuthentication

from application.codes.auth import AuthCodes
from application.Dto.auth.login import AuthLoginInputDTO
from application.Dto.auth.refresh import AuthRefreshTokenInputDTO
from application.Dto.auth.logout import AuthLogoutInputDTO


class LoginAPIView(APIView):
    """LoginAPIView"""

    http_method_names = ['post']
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    authentication_classes = []

    @inject
    def __init__(self, ioc: IAccountInteractor=None):
        self.__ioc = ioc

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        username, password = serializer.data['username'], serializer.data['password']
        with self.__ioc.login() as login:
            dto = login(AuthLoginInputDTO(
                username=username,
                password=password,
                refresh_token=get_refresh_token_cookie(request)
            ))

        code = dto.code
        if code is AuthCodes.TOKEN_PAIR_ISSUED:
            response = set_auth_cookies(
                Response(status=status.HTTP_204_NO_CONTENT),
                dto.tokens
            )
            return response

        if code is AuthCodes.USER_ALREADY_AUTHENTICATED:
            return Response(status=status.HTTP_403_FORBIDDEN, data={ 'code': code })

        return Response(status=status.HTTP_400_BAD_REQUEST, data={ 'code': code })


class RefreshAPIView(APIView):
    """RefreshAPIView"""

    http_method_names = ['post']
    authentication_classes = [CookieBasedRefreshJWTAuthentication]

    @inject
    def __init__(self, ioc: IAccountInteractor=None):
        self.__ioc = ioc

    def post(self, request: Request):
        with self.__ioc.refresh() as refresh:
            dto = refresh(AuthRefreshTokenInputDTO(
                refresh_token=get_refresh_token_cookie(request)
            ))

        code = dto.code
        if code is AuthCodes.ACCESS_TOKEN_ISSUED:
            return set_access_token_cookie(
               Response(status=status.HTTP_204_NO_CONTENT),
               dto.access
            )
        
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={ 'code': code })


class LogoutAPIView(APIView):
    """LogoutAPIView"""

    http_method_names = ['post']
    authentication_classes = [CookieBasedRefreshJWTAuthentication]

    @inject
    def __init__(self, ioc: IAccountInteractor=None):
        self.__ioc = ioc

    def post(self, request: Request):
        with self.__ioc.logout() as logout:
            logout(AuthLogoutInputDTO(
                refresh_token=get_refresh_token_cookie(request)
            ))

        response = delete_auth_cookies(
            Response(status=status.HTTP_204_NO_CONTENT)
        )
        return response


class ProtectedAPIView(APIView):
    """ProtectedAPIView"""

    def get(self, request):
        return Response(status=status.HTTP_200_OK)
