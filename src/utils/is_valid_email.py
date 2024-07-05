from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def is_valid_email(email: str) -> bool:
    """is_valid_email"""

    try:
        validate_email(email)
    except ValidationError:
        return False
    return True