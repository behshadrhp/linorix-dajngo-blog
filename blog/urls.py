from django.urls import path
from .views import index, essay, view_essay, update_essay, delete_essay


urlpatterns = [

    # index page
    path('', index, name='index'),

    # create essay
    path('essay', essay, name='essay'),

    # view essay
    path('view-essay/<slug:pk>', view_essay, name='view-essay'),

    # update essay
    path('update-essay/<slug:pk>', update_essay, name='update-essay'),

    # delete essay
    path('delete-essay/<slug:pk>', delete_essay, name='delete-essay'),

]
