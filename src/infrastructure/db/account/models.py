from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
	"""AppUser"""


class RefreshToken(models.Model):
	"""RefreshToken"""

	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	token = models.CharField(max_length=512, unique=True)
	session_name = models.CharField(max_length=255, blank=False)
	issued_at = models.DateTimeField()
	expires_at = models.DateTimeField()

	def __str__(self):
		return f'<RefreshToken user="{self.user.username}" session="{self.session_name}" />'