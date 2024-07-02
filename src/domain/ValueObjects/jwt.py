from typing import NamedTuple

from dataclasses import dataclass

from domain.ValueObjects.base import ValueObject


@dataclass(frozen=True)
class JwtToken(ValueObject[str]):
    _value: str

