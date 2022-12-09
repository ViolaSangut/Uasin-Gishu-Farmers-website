from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=user)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:Profile.objects.create(user=instance)
  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
  