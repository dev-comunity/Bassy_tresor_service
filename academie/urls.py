from django.urls import path
from .views import*

urlpatterns=[
    path('formacademicien/',SaveAcademicien,name='formacdemicien'),
    path('formcours',academicours,name='formcours'),
    path('affichecours',affichecours,name='affichecours'),
    path('acceuille_academic',home,name='acceuille_academic'),
    path('demande_Adhesion',adhesion,name='demande_Adhesion'),
    path('questionnaire',questionnaire,name='questionnaire'),
    path('reponse',reponse,name='reponse'),
    path("listdemande",listDemande,name="listdemande"),
    path('detail/<int:id_admin>',detailDemande,name='detail'),
    path('afficheacademicien',afficheacademicien,name='afficheacademicien'),
    
    
]