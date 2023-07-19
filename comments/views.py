from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from main.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        # filters on comments for a particular match
        'match',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    # use the CommentDetailSerializer in order to not have
    # to send the comment id every time we edit a comment
    # which is more optimised since comments are per match:id
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
