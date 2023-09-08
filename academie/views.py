from django.shortcuts import render,redirect
from.form import*
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from .models import Academiecours,Academicien,Questionnaire
from visitor.views import add_notifications

# Create your views here.

#fonctions de gestion academiciens 
@login_required
def SaveAcademicien(request):
    message=''
    registered=False
    if request.method=='POST':
      
        user_academicien=formAcademicien(data=request.POST)
        if user_academicien.is_valid:
            academicien=user_academicien.save()
            academicien.save()
            registered=True
            message='Votre inscription est bien enregistrée avec succes! Votre inscription sera traitée et vous rev'
            #add_notifications(request.user,'user_academic',user_academicien)
            return HttpResponseRedirect('acceuille')
        else:
            print(user_academicien.errors)
    else:
        user_academicien=formAcademicien()
        
    content={
            'message':message,
            'registered':registered,
            'form2':user_academicien,
            
        }
    return render(request,'academic/formacademicien.html',content)

@login_required
def afficheacademicien(request):
    acadmicien=Academicien.objects.all()
    return render(request,'academic/afficheacademicien.html',{'academicien':acadmicien})





#fonction d'affichage de page d'acceuille academie
@login_required
def home(request):
    return render(request,'academic/acceuille.html')




#les fonction de gestion de chat academicien
@login_required
def questionnaire(request):
    message=''
    registered=False
    if request.method=='POST':
        question=questions(data=request.POST)
        if question.is_valid:
            formquestion=question.save()
            formquestion.save()
            registered=True
            message='question envoyé avec succes!'
            #add_notifications(request.user,'question',question)
            return HttpResponseRedirect('acceuille')
        else:
            print(question.errors)
    else:
        question=questions()
    content={
        'registered':registered,
        'message':message,
        'question':question,
    }
    return render(request,'academic/questionnaire.html',content)
@login_required
def reponse(request):
    model=Questionnaire.objects.all()
    return render(request,'academic/reponse.html',{'reponse':model})



#fonction de gestion des cours academic
@login_required
def academicours(request):
    form=formAcademiecours()
    return render(request,'academic/formcours.html',{'formcours':form})


@login_required
def affichecours(request):
    cours=Academiecours.object.all()
    return render(request,'academic/affichecours.html',{'cours':cours})

#fonctions de gestion de demande de participation
@login_required
def adhesion(request):
    registered=False
    if request.method=='POST':
        form=formAdhesion(data=request.POST)
        if form.is_valid():
            enrform=form.save()
            enrform.save()
            registered=True
            #add_notifications(request.user,'form',form)
            return redirect('acceuille_academic')
        else:
            print(form.errors)
    else:
        form=formAdhesion()
    content={
        'form':form,
        'registered':registered,
    }
    return render(request,'academic/adhesion.html',content)

@login_required
def listDemande(request):
    model=Adhesion.objects.all()
    return render(request,'academic/list_demande.html',{'list':model})


@login_required
def detailDemande(request,id_admin):
    detail=Adhesion.objects.get(id=id_admin)
    return render(request,"academic/detaildemande.html",{"detail":detail})

