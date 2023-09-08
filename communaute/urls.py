from django.urls import path
from .views import*

urlpatterns=[
    path('formreve', formreve,name='formreve'),
    path('acceuillereve',homereve,name='acceuillereve'),
    path('voir_reve',affichereve,name='voir_reve'),
    path('reveform',deposReve,name='reveform'),
    path('affiche_reve',affiche,name='affiche_reve'),
]