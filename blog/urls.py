from django.urls import path
from .views import index , essay , view_essay


urlpatterns = [

    # index page
    path('' , index , name='index'),

    # create essay
    path('essay' , essay , name='essay'),

    # view essay
    path('view-essay/<slug:pk>' , view_essay , name='view-essay'),

]
