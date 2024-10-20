from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import *

 user=get_user_model()


@receiver(post_save, sender=user)
def create_user(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance)


