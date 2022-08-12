from django.urls import path
from .views import index , view_essay


urlpatterns = [

    # index page
    path('' , index , name='index'),

    # view essay
    path('view-essay/<slug:pk>' , view_essay , name='view-essay'),
]
