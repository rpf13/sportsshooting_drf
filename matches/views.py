from rest_framework import generics, permissions, filters
from main.permissions import IsOwnerOrReadOnly
from .models import Match
from .serializers import MatchSerializer


class MatchList(generics.ListCreateAPIView):
    """
    List all matches or create a match if logged in
    The perform_create method associates the match with the
    logged in user.
    """
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Match.objects.order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
