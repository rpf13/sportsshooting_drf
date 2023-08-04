from django.db import models
from django.contrib.auth.models import User


class Gun(models.Model):
    """
    Gun model, related to owner / user
    Used to create a new gun DB entry
    Choice filter for gunt type field created
    Default image and image validation
    """
    gun_filter_choices = [
        ('Handgun', 'Handgun'), ('Rifle', 'Rifle'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    gun_model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    details = models.TextField(blank=True)
    type = models.CharField(
        max_length=32, choices=gun_filter_choices, default='handgun'
    )
    image = models.ImageField(
        upload_to='images/', default='../default_event_i89yt9',
        blank=True
    )
