from rest_framework import generics, permissions, filters
from main.permissions import IsSenderOrReadOnly
from .models import Usermessage
from .serializers import UsermessageSerializer


class UsermessageList(generics.ListCreateAPIView):
    """
    List all usermessages or create a message if logged in
    The perform_create method associates the message with the
    logged in user.
    """
    serializer_class = UsermessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Usermessage.objects.all().order_by('-created_at')

    # overwrite DRF generic view to set object owner to current user
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class UsermessagesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Delete Usermessages object, if current user
    is the owner
    """
    serializer_class = UsermessageSerializer
    permission_classes = [IsSenderOrReadOnly]

    queryset = Usermessage.objects.order_by('-created_at')
