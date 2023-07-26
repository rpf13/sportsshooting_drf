from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSenderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.sender == request.user


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """
    def has_object_permission(self, request, view, obj):
        # Only allow the owner of the object to view/edit it
        return obj.owner == request.user


class IsSenderOrReceiver(permissions.BasePermission):
    """
    Custom permission to only allow the current user to access
    the messages objects if he is receiver or sender
    """
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user
