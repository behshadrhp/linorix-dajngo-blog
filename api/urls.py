from django.urls import path
from . import views

# Jason Web Token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # Jason Web Token - JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # api root
    path('', views.getRoutes, name='getResponse'),

    # Essays api
    path('essay/', views.getEssays, name='getEssays'),

    # Essays api
    path('essay/<str:pk>/', views.getEssay, name='getEssay'),

    # Vote Api
    path('essay/<str:pk>/vote/', views.essayVote, name='essayVote'),

]
