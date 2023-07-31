from django.db import models
from django.contrib.auth.models import User


class Match(models.Model):
    """
    Match model, related to owner / user
    Used to create a new match entry in DB
    Choice filter for level field created
    Default image and image validation
    """
    level_filter_choices = [
        ('Level-1', 'Level-1'), ('Level-2', 'Level-2'),
        ('Level-3', 'Level-3'), ('Level-4', 'Level-4'),
        ('Level-5', 'Level-5'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    match_date = models.DateField()
    match_location = models.CharField(max_length=255)
    division = models.CharField(max_length=255, blank=True)
    details = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_event_i89yt9',
        blank=True
    )
    level_filter = models.CharField(
        max_length=32, choices=level_filter_choices, default='Level-1'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
