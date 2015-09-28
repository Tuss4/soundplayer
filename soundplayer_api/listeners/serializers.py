from rest_framework import serializers


class ListenerLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    soundcloud_username = serializers.CharField()
