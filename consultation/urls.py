from django.urls import path
from .views import*



urlpatterns=[
    path('resultatconsultation',afficheconsultation,name='resultatconsultation'),
    path("demandeconsultation",demanderconsul,name='demandeconsultation'),
    path('acceuille',homeconsulte,name='acceuille'),
    path('reponse',Repondre_demande,name='reponse')
    
]