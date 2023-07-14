from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer

# this file replaces the views_not_generic.py, since that one was
# created without generic views, which is much more complex.


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.order_by('-created_at')
    serializer_class = ProfileSerializer


# class ProfileDetail(generics.RetrieveUpdateAPIView):
#     """
#     Retrieve or update a profile if you're the owner.
#     """
#     permission_classes = [IsOwnerOrReadOnly]
#     queryset = Profile.objects.annotate(
#         posts_count=Count('owner__post', distinct=True),
#         followers_count=Count('owner__followed', distinct=True),
#         following_count=Count('owner__following', distinct=True)
#     ).order_by('-created_at')
#     serializer_class = ProfileSerializer
