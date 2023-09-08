from django.shortcuts import render,redirect
from .form import*
from .models import*
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from visitor.views import add_notifications
# Create your views here.

@login_required
def deposReve(request):
    message=''
    if request.method=='POST':
        depos=DeposReve(data=request.POST)
        if depos.is_valid():
            ajout=depos.save()
            ajout.save()
            message='Definition de reve ajouter avec succes !'
            return redirect('affiche_reve')
        else:
            print(depos.errors)
    else:
        depos=DeposReve()
    content={
        'message':message,
        'depos':depos
    }
    return render(request,'reves/reveform.html',content)

@login_required
def affiche(request):
    reve=Reve.objects.all()
    return render(request,'reves/pageReve.html',{'RV':reve})


@login_required
def formreve(request):
    message=''
    if request.method=='POST':
        reve=Formreve(data=request.POST)
        if reve.is_valid():
            enreve=reve.save()
            enreve.save()
            message='envoyer avec succes '
            #add_notifications(request.user,'reve',reve)
        else:
            print(reve.errors)
    else:
        reve=Formreve()
    content={
        'message':message,
        'reves':reve
    }
    return render(request,'reves/formreve.html',content)


@login_required
def homereve(request):
    return render(request,'reves/acceuilereve.html')


@login_required
def affichereve(request):
    voir=DemandeReve.objects.all()
    return render(request,'reves/affichereve.html',{'voir':voir})
