from rest_framework import permissions


class PlaylistPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.listener == request.user or request.user.is_admin
