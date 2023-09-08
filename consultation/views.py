from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import formconsultation,Formreponse
from visitor.views import *
from visitor.form import userforms
from django.http import HttpResponse,HttpResponseRedirect
from .models import*
from visitor.views import add_notifications

# Create your views here.
@login_required
def demanderconsul(request):
    registered=False
    message=''
    if request.method=='POST':
        consulform=formconsultation(data=request.POST)
        user=userforms(data=request.GET)

        if consulform.is_valid():
            consulform.user=user
            consulta=consulform.save()
            consulta.save()
            registered=True
            message="consultation envoyée avec succes !"
            #add_notifications(request.user , 'consulform',consulform)
            return HttpResponseRedirect('resultatconsultation')
        else:
            consulform=formconsultation()
            return HttpResponse("Si vous n'etes pas connectés, veuillez le faire avant toute reaction s'il vous plait! ")
    else:
        consulform=formconsultation()
        
    content={
        "message":message,
        'registered':registered,
        'form':consulform,
        
    }
    
    return render(request,'consultation/formconsul.html',content)

@login_required
def homeconsulte(request):
    return render(request,'consultation/acceuilconsult.html')

@login_required
def afficheconsultation(request):
    model=Consultation.objects.all()
    return render(request,'consultation/home_demande.html',{'demande':model})

@login_required
def Repondre_demande(request):
    registered=False
    message=''
    if request.method=='POST':
        reponse=Formreponse(data=request.POST)
        if reponse.is_valid():
            ajout=reponse.save()
            ajout.save()
            redirect('resultatconsultation')
            message='Reponse envoyée avec succès !'
            registered=True
        else:
            print(reponse.errors)
    else:
        reponse=Formreponse()
    content={
        'registered':registered,
        'message':message,
        'form':reponse,

    }
    return render(request,"consultation/formreponse.html",content)

@login_required
def retourneReponse(request):
    obj=Reponse.objects.all()
    return render(request,'consultation/reponse.html',{'reponse':obj})
        
