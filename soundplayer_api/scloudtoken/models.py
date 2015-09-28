from django.db import models


class SoundcloudToken(models.Model):

    listener = models.ForeignKey('listeners.Listener', related_name='scloud_token')
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200, null=True)
    expiry = models.DateTimeField(null=True)
