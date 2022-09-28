from django.urls import path
from . import views


urlpatterns = [

    # api root
    path('', views.getRoutes, name='getResponse'),

    # Essays api
    path('essay/', views.getEssays, name='getEssays'),

    # Essays api
    path('essay/<str:pk>/', views.getEssay, name='getEssay'),

]
