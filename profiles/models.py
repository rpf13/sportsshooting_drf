from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_pabjww'
    )
    club = models.CharField(max_length=50, blank=True)
    division = models.CharField(max_length=50, blank=True)
    license = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    mail = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    social_media = models.CharField(max_length=50, blank=True)
    note = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
