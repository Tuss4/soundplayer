from django.db import models
from django.conrtib.auth.models import AbstractBaseUser


class Listener(AbstractBaseUser):

    email = models.EmailField()
    soundcloud_token = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
