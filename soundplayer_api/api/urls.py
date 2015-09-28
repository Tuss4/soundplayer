from django.conf.urls import patterns, url

import listener_api

urlpatterns = patterns(
    '',
    url(r'^listener/login/?$', listener_api.SoundCloudLogin.as_view(), name='listener_login'),
    url(r'^soundtoken/?$', listener_api.SoundCloudAuth.as_view(), name='soundcloud_token'),
)
