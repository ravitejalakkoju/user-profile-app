from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	location = models.CharField(max_length=255, null=True)
	profile_picture = models.ImageField(blank=True)
	age = models.IntegerField(null=True)
	is_subscribed = models.BooleanField(default=False)

	def full_name(self):
		return f'{self.first_name} {self.last_name}'