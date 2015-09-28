from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token


class ListenerManager(BaseUserManager):

    def create_user(self, email, password=None, scloud_uname=None):
        user = self.model(email=email)
        user.soundcloud_username = scloud_uname
        user.set_password(password)
        user.save(using=self._db)

        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, password=None, scloud_uname=None):
        user = self.create_user(email, password, scloud_uname)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user
