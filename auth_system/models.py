from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Novation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# class CastomUser(AbstractUser):
#     avatar = models.ImageField(upload_to='static/img/avatar.img', blank=True, null=True)
#     def __str__(self):
#         return self.user.username