from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendeur(models.Model):
    user=models.CharField(max_length=200,null=True,verbose_name='nom complet')
    specialite=models.CharField(max_length=200,null=True,verbose_name='votre travail')
    ville=models.CharField(max_length=100,verbose_name="ville habite")
    number=models.BigIntegerField(null=True,verbose_name="Numero de telephone")

    def __str__(self):
        return self.user.username




class Produit(models.Model):
    datedepot=models.DateTimeField(auto_now_add=True,null=True,verbose_name='date de depot')
    nom_produit=models.CharField(max_length=100,verbose_name="le nom du produit",null=True)
    typeproduit=models.CharField(max_length=100,verbose_name="le type de produit")
    caractere=models.TextField(verbose_name="decrire le produit",null=True)
    prix=models.DecimalField(null=True,decimal_places=100,max_digits=100,blank=True)
    applique=models.TextField(null=True,blank=True)
    experiente=models.DateField(auto_created=True,null=True,verbose_name="date d'experiention")

    def __str__(self):
        return self.nom_produit
    
class Demandeproduit(models.Model):
    nomproduit=models.CharField(null=True,max_length=100)
    prix=models.DecimalField(max_digits=100,decimal_places=100)
    caractere=models.TextField(blank=True,null=True)
    lieu=models.CharField(max_length=100,null=True,blank=True)
    numero=models.BigIntegerField(null=True,blank=True)


    def __str__(self):
        return self.nomproduit
    

    

