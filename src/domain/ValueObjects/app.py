from datetime import datetime

from dataclasses import dataclass

from domain.ValueObjects.base import ValueObject


@dataclass(frozen=True)
class AppDateTime(ValueObject[datetime]):
    _value: datetime