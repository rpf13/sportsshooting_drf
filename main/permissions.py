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
