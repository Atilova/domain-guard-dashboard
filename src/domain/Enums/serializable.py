from enum import Enum


class SerializableEnum(Enum):
    """SerializableEnum"""

    def __str__(self):
        return str(self.value)

    @classmethod
    def from_str(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f'{value} is not a valid {cls.__name__}')