from django.db import models


# Create your models here.
class Astuce (models.Model):
    titre=models.CharField(max_length=200,blank=True,null=True)
    astuce=models.TextField(null=True)
    media=models.FileField(upload_to=True,null=True,default=True,blank=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.titre