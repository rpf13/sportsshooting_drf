from rest_framework import generics, permissions, filters
from main.permissions import IsOwnerOrReadOnly
from attendings.models import Attending
from attendings.serializers import AttendingSerializer


class AttendingList(generics.ListCreateAPIView):
    """
    List all Attendings or create an attending object,
    if logged in. The perform_create method associates the
    attending object with the logged in user
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttendingSerializer
    queryset = Attending.objects.all().order_by('-created_at')

    # overwrite DRF generic view to set object owner to current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendingDetail(generics.RetrieveDestroyAPIView):
    # only the owner can delete an attending object
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendingSerializer
    queryset = Attending.objects.all()
