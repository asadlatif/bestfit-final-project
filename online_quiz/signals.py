from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # print("Profile Created")

# post_save.connect(create_profile, sender=User)
@receiver (post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created ==   False:
        instance.profile.save()
        # print("Profile Updated")
        # try:
        #     instance.profile.save()
        #     print("Profile Updated")
        # except:
        #     Profile.objects.create(user=instance)
        #     print("Profile Created for Existing user")