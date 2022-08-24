from django.urls import path
from .views import user

urlpatterns = [
    
    # user page
    path('' , user, name='user'),

]
