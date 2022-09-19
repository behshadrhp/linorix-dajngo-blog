from django.urls import path, re_path
from . import views

urlpatterns = [

    # user page
    path('', views.user, name='user'),

    # profile user
    re_path(r'author/(?P<pk>[-\w]+)/', views.user_profile, name='profile-username'),

    # login page
    path('login', views.user_login, name='login'),

    # logout user
    path('logout', views.user_logout, name='logout'),

    # Register user
    path('register', views.user_register, name='register'),

    # Account user
    path('account', views.user_account, name='account'),

    # Edit information Account
    path('update-information', views.update_profile, name='update-profile'),

    # update Skill
    path('update-skill/<str:pk>', views.update_skill, name='update-skill'),

    # create Skill
    path('skill', views.create_skill, name='skill'),

    # delete skill
    path('delete-skill/<str:pk>', views.delete_skill, name='delete-skill'),

    # inbox
    path('inbox/', views.inbox, name='inbox'),

    # inbox message
    path('inbox/message/<str:pk>', views.inbox_message, name='inbox-message'),

    # message form
    re_path(r'message-form/(?P<pk>[-\w]+)', views.message_form, name='message-form'),

]
