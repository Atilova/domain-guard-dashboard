import os

from datetime import timedelta

from dataclasses import dataclass, field


@dataclass
class DjangoAppConfig:
    """DjangoAppConfig"""

    environment: str = 'development'
    settings_module: str = field(init=False)

    def __post_init__(self):
        self.settings_module = f'infrastructure.settings.{self.environment}'


@dataclass
class JwtAuthConfig:
    """JwtAuthConfig"""

    secret: str
    algorithm: str = 'HS256'
    access_token_expiration_delta: timedelta = timedelta(minutes=10)
    refresh_token_expiration_delta: timedelta = timedelta(days=7)
    http_only_cookie: bool = True
    strict_origin_cookie: bool = True


@dataclass
class AppConfig:
    """AppConfig"""

    django: DjangoAppConfig
    jwt_auth: JwtAuthConfig


def load_django_app_config() -> DjangoAppConfig:
    """load_django_app_config"""

    # Todo: load from env
    return DjangoAppConfig(
        environment='development'
    )

def load_jwt_auth_config() -> JwtAuthConfig:
    """load_jwt_auth_config"""

    # Todo: load from env
    return JwtAuthConfig(
        secret='unsafe_secrete'
    )

def load() -> AppConfig:
    """load"""

    return AppConfig(
        django=load_django_app_config(),
        jwt_auth=load_jwt_auth_config()
    )