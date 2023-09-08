from django.urls import path
from .views import*


urlpatterns=[
    path('',acceuil,name='acceuil'),
    path('login/',user_login,name='login'),
    path('register/',register,name='register'),
    path('logout/',user_logout,name='logout'),
    path("recherche",recherche_generale,name='recherche')
]