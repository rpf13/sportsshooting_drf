from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticated
from main.permissions import IsOwner
from .models import Gun
from .serializers import GunSerializer


class GunList(generics.ListCreateAPIView):
    """
    Loggend in and Owner required
    List all guns or create a gun entry if logged in
    The perform_create method associates the gun with the
    logged in user.
    """
    serializer_class = GunSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        return Gun.objects.filter(
            owner=self.request.user
            ).order_by('-created_at')

    def get_permissions(self):
        return [IsAuthenticated(), IsOwner()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GunDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GunSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_permissions(self):
        return [IsAuthenticated(), IsOwner()]

    def get_queryset(self):
        return Gun.objects.filter(owner=self.request.user)