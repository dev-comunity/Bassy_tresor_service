from django.urls import path
from .views import*

urlpatterns=[
    path('formastuce',deposerastuce,name='formastuce'),
    path('acceuilleastuce',homeastuce,name='acceuilleastuce'),
    path('afficheastuce',voirAstuce,name='afficheastuce'),
]