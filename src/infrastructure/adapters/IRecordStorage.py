from typing import (
    Protocol,
    Optional,
    TypeVar,
)


KeyT = TypeVar('KeyT', bound=str)
ValueT = TypeVar('ValueT', str, bytes)


class IRecordStorage(Protocol[KeyT, ValueT]):
    """IRecordStorage"""

    def ping(self) -> bool:
        pass

    def insert(self, key: KeyT, value: ValueT, ttl: Optional[int]=None) -> None:
        pass

    def retrieve(self, key: KeyT) -> Optional[ValueT]:
        pass

    def update(self, key: KeyT, updated: ValueT, ttl: Optional[int]=None) -> None:
        pass

    def delete(self, key: KeyT) -> bool:
        pass

    def exists(self, key: KeyT) -> bool:
        pass

    def set_expire(self, key: KeyT, ttl: int) -> None:
        pass
