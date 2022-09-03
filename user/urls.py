from django.urls import path
from .views import user, user_profile, user_login, user_logout, user_register, user_account, update_profile

urlpatterns = [

    # user page
    path('', user, name='user'),

    # profile user
    path('author/<slug:pk>', user_profile, name='profile-username'),

    # login page
    path('login', user_login, name='login'),

    # logout user
    path('logout', user_logout, name='logout'),

    # Register user
    path('register', user_register, name='register'),

    # Account user
    path('account', user_account, name='account'),

    # Edit information Account
    path('update-information', update_profile, name='update-profile'),

]
