from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


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

        # Send Message TODO SMTP service
        # subject = 'ٌHello, Welcome to your home'
        # message = 'We are a family'
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email],
        #     fail_silently=False,
        # )

# Connection for save profile
post_save.connect(create_profile, sender=User)

# update profile
def update_profile(sender, instance, created, **kwargs):
    
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.full_name
        user.username = profile.username
        user.email = profile.email
        user.slug = profile.slug
        user.save()

# connection for update profile
post_save.connect(update_profile, sender=Profile)

# Delete Profile User
def delete_profile(sender, instance, **kwargs):

    user = instance.user
    user.delete()

# Connection for delete profile
post_delete.connect(delete_profile, sender=Profile)