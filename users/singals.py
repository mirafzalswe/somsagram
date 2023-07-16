from django.db.models import signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signals.post_save, sender = User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()
