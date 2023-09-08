from django.shortcuts import render,redirect
from .forms import userProduit,userVendeur,demande
from django.http import HttpResponse
from .models import*
from visitor.views import add_notifications
from django.contrib.auth.decorators import login_required

#fonction qui gere les vendeurs de produit

@login_required
def SaveVendeur(request):
    registered=False
    message=''
    if request.methode=="POST":
        
        user_vendeur=userVendeur(data=request.POST)
        if user_vendeur.is_valid():
            vendeur=user_vendeur.save()
            vendeur.save()
            registered=True
            message='Vous venez de deposer un produit avec réussite !'
            add_notifications(request.user,'user_vendeur',user_vendeur)
           
        else:
            return HttpResponse(user_vendeur.errors)
    else:
      
        user_vendeur=userVendeur()
    content={
            'form2':user_vendeur,
            'message':message,
            'register':registered,
        }

    return render(request,'produits/formsvendeur.html',content)


@login_required
def AfficheVendeur(request):
    vendeurs=Vendeur.objects.all()
    return render(request,'produits/vendeurs.html',{'vendeur':vendeurs})


@login_required
def detailvendeur(request,id_admin):
    detail=Vendeur.objects.get(id=id_admin)
    return render(request,'produits/deailvendeur.html',{'detail':detail})




#fonctions qui gèrent les demandes de produit
@login_required
def demandeproduit(request):
    message=''
    if request.method=='POST':
        fomrdemande=demande(data=request.POST)
        if fomrdemande.is_valid():
            mydemande=fomrdemande.save()
            mydemande.save()
            message='demande envoyée avec succes !'
            add_notifications(request.user,'formdemande',fomrdemande)
            return redirect('homeproduit')
        else:
            print(fomrdemande.errors)
    else:
        fomrdemande=demande()
    content={
        'message':message,
        'form':fomrdemande,
    }
    return render(request,'produits/demandeproduit.html',content)

@login_required
def reponseDemande(request):
    model=Demandeproduit.objects.all()
    return render(request,"produits/list_demande.html",{"reponse":model})



#fonctions qui gèrent les stock de produit
@login_required
def Saveproduit(request):
    message=''
    if request.methode=='POST':
        formproduit=userProduit(data=request.POST)
        if formproduit.is_valid():
            produit=formproduit.save()
            produit.save()
            message='vous venez de deposer un produit avec succes'
            #add_notifications(request.user,'formproduit',formproduit)
            return redirect('affiche_produit')
        else:
            return HttpResponse(formproduit.errors)
    else:
        formproduit=userProduit()
    content={
        'form':formproduit,
        'message':message
    }
    return render(request,'produits/formproduit.html',content)

@login_required
def Afficheproduits(request):
    produit=Produit.objects.all()
    return render(request,'Produits/pageproduit.html',{'produit':produit})




#fonction qui gère la page d'acceuille de produit
@login_required
def homeproduit(request):
    return render(request,'produits/acceuilleproduit.html')
