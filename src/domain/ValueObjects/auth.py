from dataclasses import dataclass

from domain.ValueObjects.base import ValueObject


@dataclass(frozen=True)
class AppUserId(ValueObject[int]):
    _value: int


@dataclass(frozen=True)
class AppUserEmail(ValueObject[str]):
    _value: str


@dataclass(frozen=True)
class AppUserUsername(ValueObject[str]):
    _value: str


@dataclass(frozen=True)
class AppUserFirstName(ValueObject[str]):
    _value: str


@dataclass(frozen=True)
class AppUserPassword(ValueObject[str]):
    _value: str
