from django.db import models
from unidecode import unidecode
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from django_quill.fields import QuillField
from user.models import Profile
import uuid


# Create your models here.


class Essay(models.Model):
    '''This class is for create essay .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    # information
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, unique=True)
    description = QuillField()
    upload_image = models.ImageField(default='surface.jpg')
    source_link = models.CharField(max_length=2048, blank=True, null=True)
    demo_link = models.CharField(max_length=2048, blank=True, null=True)
    total_vote = models.IntegerField(default=0)
    positive_vote = models.IntegerField(
        default=0, validators=[MaxValueValidator(100)])

    # relation
    tag = models.ManyToManyField('Tag', related_name='+')

    # slug url
    slug = models.SlugField(max_length=70, unique=True, allow_unicode=True)


    # unicode fixed
    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    # return the title of the class
    def __str__(self):
        return self.title

    # Meta class for change and development
    class Meta:
        ordering = ['-positive_vote', '-total_vote', 'title', '-created']

    @property
    def reviewers(self):
        queryset = self.comment_set.all().values_list('owner__username', flat=True)
        return queryset

    @property
    def VoteCount(self):
        comment = self.comment_set.all()
        up_vote = comment.filter(value='up').count()
        
        total_votes = comment.count()
        positive_votes = (up_vote/total_votes) * 100

        self.total_vote = total_votes
        self.positive_vote = positive_votes
        self.save()

class Comment(models.Model):
    '''This class is for commenting below the essay .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateField(auto_now=True, editable=False)

    # selection of type vote
    VOTE = [
        ('up', 'up vote'),
        ('down', 'down vote')
    ]

    # information 
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    essay = models.ForeignKey('Essay', on_delete=models.CASCADE, null=True, blank=True)

    body = models.TextField(max_length=300)

    # user comment
    value = models.CharField(
        choices=VOTE, default='up', max_length=10)

    # return the commit of the class
    def __str__(self):
        return self.value

    # Meta class for change and development
    class Meta:
        ordering = ['-created']
        unique_together = [['owner','essay']]


class Tag(models.Model):
    '''This class is for marking Essay .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateField(auto_now=True, editable=False)

    # title label
    label = models.CharField(max_length=15, unique=True)

    # return the label of the class
    def __str__(self):
        return self.label

    # Meta class for change and development
    class Meta:
        ordering = ['-created']
