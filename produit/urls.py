from django.urls import path
from .views import* 


urlpatterns=[
    path('affiche_produit',Afficheproduits,name='affiche_produit'),
    path("homeproduit",homeproduit,name='homeproduit'),
    path('demandeproduit',demandeproduit,name='demandeproduit'),
    path('deposer_produit',Saveproduit,name='deposer_produit'),
    path('enregistrer_vendeur',SaveVendeur,name='enregistrer_vendeur'),
    path('affiche_vendeur',AfficheVendeur,name='affiche_vendeur'),
    path("reponsedemande",reponseDemande,name="reponsedemande"),
    path('detail/<int:id_admin>',detailvendeur,name='detail')

]