from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import ListenerManager


class Listener(AbstractBaseUser):

    email = models.EmailField(unique=True)
    soundcloud_username = models.CharField(max_length=200, unique=True)
    soundcloud_token = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = ListenerManager()

    def __unicode__(self):
        return self.email

    class Meta:
        unique_together = ('email', 'soundcloud_username')
