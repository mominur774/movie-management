from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from enum_helper import GenderChoices

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=GenderChoices.choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
