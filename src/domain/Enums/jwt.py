from .serializable import SerializableEnum


class JwtTokenType(SerializableEnum):
    """JwtTokenType"""

    APP_ACCESS = 'app_access'
    APP_REFRESH = 'app_refresh'