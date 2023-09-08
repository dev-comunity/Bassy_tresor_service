from django.db import models

# Create your models here.
class Reve(models.Model):
    objet=models.CharField(max_length=100,null=True,blank=True)
    desc=models.TextField(null=True,verbose_name='Description de reve')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.objet


class DemandeReve(models.Model):
    datereve=models.DateTimeField(auto_created=True,verbose_name='l\'heure et la date du reve')
    decrire=models.TextField(null=True )
    adress=models.EmailField(blank=True)
    numero=models.CharField(max_length=10)
    def __str__(self):
        return self.numero

