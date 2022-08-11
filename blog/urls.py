from django.urls import path
from .views import index


urlpatterns = [

    # index page
    path('' , index , name='index'),
]
