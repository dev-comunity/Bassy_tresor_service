from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your models here.


class Academicien(LoginRequiredMixin,models.Model):
    nom=models.CharField(max_length=200,null=True,verbose_name='votre nom complet')
    number=models.BigIntegerField(null=True,verbose_name='numero de telephone')
    ville=models.CharField(max_length=100,verbose_name='ville habite',null=True )
    age=models.DateField(auto_created=True,null=True)
    apprendre1='apprendre en ligne'
    apprendre2='apprendre en presentiel'
    typeapprendre=[
        (apprendre1,'apprendre en ligne'),(apprendre2,'apprendre en presentiel')
    ]
    modeapprend=models.CharField(max_length=100,choices=typeapprendre,default=apprendre1,null=True)

    def __str__(self):
        return self.nom
    

class Questionnaire(LoginRequiredMixin,models.Model):
    
    question=models.TextField(null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.utilisateur

class Academiecours(LoginRequiredMixin,models.Model):
    titre=models.CharField(max_length=200,null=True,blank=True)
    image_cours=models.ImageField(upload_to=True,blank=True,null=True)
    deposer_lesson=models.FileField(upload_to=True,blank=True)
    ecrire_lesson=models.TextField( null=True,blank=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
class Adhesion(LoginRequiredMixin,models.Model):
    #nom=models.CharField(max_length=100,null=True)
    #prenom=models.CharField(max_length=100,null=True)
    objet=models.CharField(max_length=200,null=True,blank=True)
    demande=models.TextField(null=True)
    mode1='participation en ligne'
    mode2='participation en presentielle'
    typechoix=[
        (mode1,'participation en ligne'),(mode2,'participation en presentielle')
    ] 
    mode=models.CharField(max_length=200,choices=typechoix,default=mode2)
    adress=models.CharField(max_length=200,null=True,blank=True)
    numero=models.CharField(max_length=20,null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.objet
