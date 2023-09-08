from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class User(AbstractUser):
    is_visitor=models.BooleanField(default=True)
    is_academicien=models.BooleanField(default=False)
    is_vendeur=models.BooleanField(default=False)
    is_professionel=models.BooleanField(default=False)
    #is_administor=models.BooleanField(default=False)
    is_formateur=models.BooleanField(default=False)

class Notifications(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='notifie')
    actipon=models.CharField(max_length=255,null=True)
    read =models.BooleanField(default=False,null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    update=models.DateTimeField(auto_now=True,null=True)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,
                                   related_name='obj',null=True,blank=True)
    objet_id=models.IntegerField(null=True,blank=True)
    target=GenericForeignKey('content_type','objet_id')

    class Meta:
        ordering=['-created']
        indexes=[
            models.Index(fields=['read']),
            models.Index(fields=['content_type','objet_id'])
        ]

    def __str__(self):
        return "%s-%s-%s-%s"%(self.user,self.actipon,self.target.content,self.created)


