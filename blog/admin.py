from django.contrib import admin
from .models import Essays, Comments, Tags

# Register your models here.

admin.site.register(Essays)
admin.site.register(Comments)
admin.site.register(Tags)
