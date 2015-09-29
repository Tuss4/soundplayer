from rest_framework import views, status
from rest_framework.response import Response

import soundcloud


class ListPlaylistsView(views.APIView):

    def get(self, request, *args, **kwargs):

        token = request.user.scloud_token.access_token
        client = soundcloud.Client(access_token=token)
        playlists = client.get('/me/playlists')
        plist = [dict(title=p.title, id=p.id) for p in playlists]
        return Response(dict(results=plist), status=status.HTTP_200_OK)
