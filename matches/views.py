from django.db.models import Count
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
    # serializer_class will result rendered form in browser
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Match.objects.annotate(
        comments_count=Count('comment', distinct=True),
        attendings_count=Count('attendings', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = [
        'comments_count',
        'attendings_count',
    ]
    search_fields = [
        'owner__username',
        'title',
        'match_date',
        'match_location',
    ]

    # overwrite DRF generic view to set object owner to current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Delete Match object, if current user
    is the owner
    """
    serializer_class = MatchSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Match.objects.annotate(
        comments_count=Count('comment', distinct=True),
        attendings_count=Count('attendings', distinct=True)
    ).order_by('-created_at')
