from django.db import models
from django.contrib.auth.models import User
from matches.models import Match


class Comment(models.Model):
    """
    Comment model, related to User and Match
    Used to create a new comment for a
    particular match in the match detail view
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment
