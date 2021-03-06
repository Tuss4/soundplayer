from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import soundcloud

from django.conf import settings
from listeners.models import Listener
from listeners.serializers import ListenerLoginSerializer
from playlists.models import Playlist
from scloudtoken.models import SoundcloudToken


SOUNDCLIENT = soundcloud.Client(
    client_id=settings.SOUNDCLOUD_CLIENT_ID,
    client_secret=settings.SOUNDCLOUD_SECRET,
    redirect_uri=settings.SOUNDCLOUD_REDIRECT_URL
)


class SoundCloudLogin(views.APIView):

    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):

        serializer = ListenerLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            l = Listener.objects.get(email=serializer.data.get('email'))
            return Response(dict(id=l.pk, token=l.auth_token.key), status=status.HTTP_200_OK)
        except Listener.DoesNotExist:
            l = Listener.objects.create_user(
                email=serializer.data.get('email'),
                scloud_uname=serializer.data.get('soundcloud_username').lower())
            r = {
                "redirect_url": SOUNDCLIENT.authorize_url(),
                "id": l.pk,
                "token": l.auth_token.key
            }
            return Response(r, status=status.HTTP_201_CREATED)


class SoundCloudAuth(views.APIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code:
            token = SOUNDCLIENT.exchange_token(code)
            client = soundcloud.Client(access_token=token.access_token)
            listener_name = client.get('/me').username
            try:
                l = Listener.objects.get(soundcloud_username=listener_name.lower())
                SoundcloudToken.objects.create(
                    listener=l,
                    access_token=token.access_token,
                )
                playlists = client.get('/me/playlists')
                for p in playlists:
                    embed = client.get('/oembed', url=p.permalink_url)
                    Playlist.objects.create(
                        listener=l,
                        scloud_id=p.id,
                        title=p.title,
                        scloud_url=p.permalink_url,
                        embed_code=embed.html
                    )
            except Listener.DoesNotExist:
                return Response(
                    dict(detail="Listener not found."), status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)
