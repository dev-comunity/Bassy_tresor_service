from django.db import models
from visitor.models import User

# Create your models here.
class Consultation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    objet=models.CharField(max_length=50,blank=True)
    Description=models.TextField(null=True) 
    consula1='une consultation en ligne'
    consula2='une consultation en presentielle'
    modeconsula=[(consula1,'une consultation en ligne'),(consula2,'une consultation en presentielle')]
    mode=models.CharField(choices=modeconsula,default=consula1,max_length=100)
    temps=models.DateTimeField(auto_now_add=True)
    numero=models.CharField(max_length=20)
    adress=models.EmailField()

    def __str__(self):
        return self.nom
    

class Reponse(models.Model):
    nom=models.CharField(max_length=50)
    son_but=models.CharField(max_length=200)
    desc=models.TextField()
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
        