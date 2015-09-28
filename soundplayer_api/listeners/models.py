from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Listener(AbstractBaseUser):

    email = models.EmailField(unique=True)
    soundcloud_token = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
