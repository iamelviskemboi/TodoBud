from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


# POST-REGISTRATION SIGNAL
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# POST-PROFILE-UPDATE SIGNAL
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
