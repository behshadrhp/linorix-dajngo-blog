from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid
import random

# Create your models here.

class Profile(models.Model):
    '''This class is create user profile .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    # avatar
    avatar_image = random.randint(1,7)
    avatar = models.ImageField(default=f'/static/avatar/{avatar_image}.png' , upload_to='profile/')

    # information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=25, unique=True)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=30 , unique=True)
    specialty = models.CharField(max_length=30)

    # BIO
    bio = models.TextField()

    # Social Network
    github = models.CharField(max_length=25 , null=True , blank=True )
    twitter = models.CharField(max_length=25 , null=True , blank=True )
    linkedin = models.CharField(max_length=25 , null=True , blank=True )
    instagram = models.CharField(max_length=25 , null=True , blank=True )
    telegram = models.CharField(max_length=25 , null=True , blank=True )
    website = models.CharField(max_length=25 , null=True , blank=True )

    # slug url
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(Profile, self).save(*args, **kwargs)

    # return the title of the class
    def __str__(self):
        return str(self.user)