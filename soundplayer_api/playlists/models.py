from django.db import models
from django.conf import settings

import soundcloud


CLIENT = soundcloud.Client(client_id=settings.SOUNDCLOUD_CLIENT_ID)


class Playlist(models.Model):

    listener = models.ForeignKey('listeners.Listener', related_name='playlists')
    scloud_id = models.IntegerField()
    title = models.CharField(max_length=100)
    scloud_url = models.URLField()
    embed_code = models.TextField()

    class Meta:
        unique_together = ('listener', 'scloud_id')

    def get_embed_code(self):
        embed_info = CLIENT.get('/oembed', url=self.scloud_url)
        return embed_info.html
