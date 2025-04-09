from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[('1', 'Admin'), ('2', 'muharrir'), ('3', 'user')], default=3)