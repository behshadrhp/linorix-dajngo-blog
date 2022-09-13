from django.urls import path, re_path
from .views import index, essay, view_essay, update_essay, delete_essay


urlpatterns = [

    # index page
    path('', index, name='index'),

    # create essay
    path('essay', essay, name='essay'),

    # view essay
    re_path(r'view-essay/(?P<pk>[-\w]+)/', view_essay, name='view-essay'),

    # update essay
    re_path(r'update-essay/(?P<pk>[-\w]+)/', update_essay, name='update-essay'),

    # delete essay
    re_path(r'delete-essay/(?P<pk>[-\w]+)/', delete_essay, name='delete-essay'),

]
