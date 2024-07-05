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
class RedisConfig:
    """RedisConfig"""

    host: str
    port: int = 6379
    user: str = ''
    password: str = ''
    uri: str = field(init=False)

    def __post_init__(self):
        self.uri = f'redis://{self.user}:{self.password}@{self.host}:{self.port}/'

    def get_db_uri(self, db):
        return f'{self.uri}{db}'


@dataclass
class AppConfig:
    """AppConfig"""

    django: DjangoAppConfig
    jwt_auth: JwtAuthConfig
    redis: RedisConfig


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

def load_redis_config() -> RedisConfig:
    """load_redis_config"""

    host: str = os.environ.get('REDIS_HOST', 'localhost')
    port: int = int(os.environ.get('REDIS_PORT', 6379))
    user: str = os.environ.get('REDIS_USER', '')
    password: str = os.environ.get('REDIS_PASSWORD', '')

    return RedisConfig(
        host=host,
        port=port,
        user=user,
        password=password
    )

def load() -> AppConfig:
    """load"""

    return AppConfig(
        django=load_django_app_config(),
        jwt_auth=load_jwt_auth_config(),
        redis=load_redis_config()
    )