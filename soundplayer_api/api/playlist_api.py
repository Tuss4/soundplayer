from rest_framework import generics, status
from rest_framework.response import Response

import soundcloud

from playlists.serializers import PlaylistSerializer
from playlists.models import Playlist


class ListPlaylistsView(generics.ListAPIView):

    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(listener=self.request.user)


class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_url_kwarg = 'playlist_pk'
