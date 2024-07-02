from random import choice

from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import RefreshToken


SESSION_NAMES = [
    'Serene Grove',
    'Whispering Pines',
    'Crystal Waters',
    'Moonlit Meadow',
    'Starlight Summit',
    'Enchanted Forest',
    'Ocean Breeze',
    'Golden Sunset',
    'Misty Valley',
    'Tranquil Haven'

    # Todo: add more
]

def _new_session_name():
    """_new_session_name"""

    return choice(SESSION_NAMES)

@receiver(pre_save, sender=RefreshToken)
def add_session_name(sender, instance: RefreshToken, *args, **kwargs):
    if not instance.session_name:
        instance.session_name = _new_session_name()
        