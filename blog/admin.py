from django.contrib import admin
from .models import Essay, Comment, Tag

# Register your models here.

admin.site.register(Essay)
admin.site.register(Comment)
admin.site.register(Tag)
