from django.db import models
from django.contrib.auth.models import User
from matches.models import Match


class Attending(models.Model):
    """
    Attending model, related to User and Match
    'unique_together' makes sure a user can't attend the
    same match twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(
        Match, related_name='attendings', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'match']

    def __str__(self):
        return f'{self.owner} {self.match}'
