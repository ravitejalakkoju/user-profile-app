from django.db import models
from django.contrib.auth.models import AbstractUser

def validate_unique_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError("Email already exists.")

class User(AbstractUser):
	email = models.EmailField(max_length=254, null = True, unique=True, validators=[])
	location = models.CharField(max_length=255, null=True)
	profile_picture = models.ImageField(blank=True)
	age = models.IntegerField(null=True)
	is_subscribed = models.BooleanField(default=False)