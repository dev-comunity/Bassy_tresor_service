from django.shortcuts import render,redirect
from .form import userforms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import*

from django.db.models import Q
from academie.models import*  # Importez les modèles nécessaires
from astuce.models import*
from consultation.models import*
from produit.models import*
from communaute.models import*
from django.contrib.auth.decorators import login_required

# Create your views here.

def acceuil(request):

    return render(request,'utilisateurs/acceuil.html')


def register(request):
    registered=False
    if request.method=='POST':
        usersave=userforms(data=request.POST)
        if usersave.is_valid():
            user=usersave.save()
            user.save()
            registered=True
            #add_notifications(request.user, 'user_name', user_name)
            return redirect('login')
        else:
            print(user_name.errors)
    else:
        user_name=userforms()
       
    content={
        'register':registered,
        'form1':user_name,
        
    }
    return render(request, 'utilisateurs/register.html',content)
    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else :
                return HttpResponse("L'utilisateur est desactivé")
        else:
            return HttpResponse("le nom d'utilisateur ou le mot de passe est incorrect")
    else:
        return render(request,'utilisateurs/login.html')
    
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_notifications(user,action,target):
    notif=Notifications(user=user,action=action,target=target)
    notif.save()



#FONCTION DE RECHERCHE


@login_required
def recherche_generale(request):
    query = request.GET.get('q', '')  # Récupérez la requête de recherche depuis les paramètres GET

    # Construisez une requête complexe pour chercher dans différents champs de différents modèles
    results = []
    if query:

        
 # Recherche dans Questionnaire
        results +=Questionnaire.objects.filter(
            Q(question__icontains=query) 
        )


 # Recherche dans DemandeReve
        results += DemandeReve.objects.filter(
            Q(decrire__icontains=query)
        )

# Recherche dans Reve
        results += Reve.objects.filter(
            Q(objet__icontains=query) | Q(desc__icontains=query)
        )

# Recherche dans Astuce
        results += Astuce.objects.filter(
            Q(titre__icontains=query) | Q(astuce__icontains=query)
        )



# Recherche dans Produit
        results += Produit.objects.filter(
            Q(nom_produit__icontains=query) | Q(typeproduit__icontains=query)|Q(caractere__icontains=query)
        )

# Recherche dans Demandeproduit
        results += Demandeproduit.objects.filter(
            Q(nomproduit__icontains=query) | Q(caractere__icontains=query)
        )


    # Renvoyez les résultats à un template ou sous une autre forme appropriée
    return render(request, 'utilisateurs/recherche.html', {'results': results, 'query': query})
