from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile


# create signal models

# Create user Profile 
def create_profile(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            full_name=f"{user.first_name} {user.last_name}",
            username=user.username,
            email=user.email,
            
        )

# delete user Profile
def delete_profile(sender, instance, **kwargs):

    user = instance.user
    user.delete()


# connection for Create user Profile
post_save.connect(create_profile, sender=User)

# connection for Delete user Profile
post_delete.connect(delete_profile, sender=Profile)