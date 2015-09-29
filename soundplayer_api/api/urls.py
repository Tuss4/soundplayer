from django.conf.urls import patterns, url

import listener_api
import playlist_api


urlpatterns = patterns(
    '',
    url(r'^listener/login/?$', listener_api.SoundCloudLogin.as_view(), name='listener_login'),
    url(r'^soundtoken/?$', listener_api.SoundCloudAuth.as_view(), name='soundcloud_token'),
    url(r'^playlists/?$', playlist_api.ListPlaylistsView.as_view(), name='list_playlists'),
    url(
        r'^playlists/(?P<playlist_pk>\d+)/?$',
        playlist_api.PlaylistDetailView.as_view(), name='playlist_detail'),
)
