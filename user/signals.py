from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from .models import Profile


# Signal Models

# Create Profile User
def create_profile(sender, instance, created, **kwargs):

    user = instance
    
    if created:
        
        profile = Profile.objects.create(
            user=user,
            full_name=f'{user.first_name} {user.last_name}',
            username=user.username,
            email=user.email,
        )

# Connection for save profile
post_save.connect(create_profile, sender=User)

# Delete Profile User
def delete_profile(sender, instance, **kwargs):

    user = instance.user
    user.delete()

# Connection for delete profile
post_delete.connect(delete_profile, sender=Profile)