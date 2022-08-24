from django.urls import path
from .views import user , user_profile

urlpatterns = [
    
    # user page
    path('' , user, name='user'),

    # profile user
    path('<slug:pk>', user_profile, name='profile-username'),

]
