from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Novation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

