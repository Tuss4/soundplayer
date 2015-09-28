from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import soundcloud

from django.conf import settings


SOUNDCLIENT = soundcloud.Client(
    client_id=settings.SOUNDCLOUD_ID,
    client_secret=settings.SOUNDCLOUD_SECRET,
    redirect_uri=settings.SOUNDCLOUD_REDIRECT_URL
)


class SoundCloudLogin(views.APIView):

    permission_classe = (AllowAny, )

    def get(self, request, *args, **kwargs):
        return Response(
            {"redirect_url": SOUNDCLIENT.authorize_url()}, status=status.HTTP_200_OK)


class SoundCloudAuth(views.APIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        print request.query_params
        return Resposne(status=status.HTTP_200_OK)
