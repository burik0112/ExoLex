from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
