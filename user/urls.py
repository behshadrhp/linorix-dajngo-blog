from django.urls import path
from .views import user, user_profile, user_login, user_logout

urlpatterns = [
    
    # user page
    path('' , user, name='user'),

    # profile user
    path('author/<slug:pk>', user_profile, name='profile-username'),

    # login page
    path('login', user_login, name='login'),

    # logout user
    path('logout', user_logout, name='logout'),

]
