from redis import Redis

from typing import (
    Optional,
    Callable,
    TypeVar,
    Generic
)

from .errors import StorageCRUDError


KeyT = TypeVar('KeyT', bound=str)
ValueT = TypeVar('ValueT', str, bytes)

def _add_prefix(prefix: str) -> Callable[[KeyT], str]:
    """_add_prefix"""

    return lambda key: f'{prefix}:{key}'


class RedisRecordStorage(Generic[KeyT, ValueT]):
    """RedisRecordStorage"""

    def __init__(self, *, prefix: str, client: Redis, key='data'):
        self.__client = client
        self.__value_key = key
        self.__add_prefix = _add_prefix(prefix)

    def ping(self) -> bool:
        return self.__client.ping()

    def insert(self, key: KeyT, value: ValueT, ttl: Optional[int]=None) -> None:
        record_key = self.__add_prefix(key)
        try:
            encoded = value.encode()
            self.__client.hset(record_key, key=self.__value_key, value=encoded)
        except (AttributeError, TypeError) as exp:
            raise StorageCRUDError(f'Storage insert() failed to encode data for "{record_key}" key.') from exp
        except Exception as exp:
            raise StorageCRUDError(f'Storage failed to insert to "{record_key}" key.') from exp

        if isinstance(ttl, int): self.set_expire(key, ttl)

    def retrieve(self, key: KeyT) -> Optional[ValueT]:
        if not self.exists(key): return None

        record_key = self.__add_prefix(key)
        try:
            data: bytes = self.__client.hget(record_key, key=self.__value_key)
            decoded = data.decode()
        except Exception as exp:
            raise StorageCRUDError(f'Storage failed to retrieve by "{record_key}" key.') from exp
        return decoded

    def update(self, key: KeyT, updated: ValueT, ttl: Optional[int]=None) -> None:
        if not self.exists(key): return
        return self.insert(key, updated, ttl)

    def delete(self, key: KeyT) -> bool:
        if not self.exists(key): return False

        record_key = self.__add_prefix(key)
        try:
            deleted = self.__client.delete(record_key)
        except Exception as exp:
            raise StorageCRUDError(f'Storage failed to delete "{record_key}" key.') from exp
        return bool(deleted)

    def exists(self, key: KeyT) -> bool:
        record_key = self.__add_prefix(key)
        try:
            is_exists = self.__client.hexists(record_key, key=self.__value_key)
        except Exception as exp:
            raise StorageCRUDError(f'Storage exists() failed for "{record_key}" key.') from exp
        return is_exists

    def set_expire(self, key: KeyT, ttl: int) -> None:
        if not self.exists(key): return

        record_key = self.__add_prefix(key)
        try:
            self.__client.expire(record_key, ttl)
        except Exception as exp:
            raise StorageCRUDError(f'Storage set_ttl() failed for "{record_key}" key.') from exp
