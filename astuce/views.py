from django.shortcuts import render
from .form import*

from django.contrib.auth.decorators import login_required
from visitor.views import add_notifications
# Create your views here.

@login_required
def deposerastuce(request):
    if request.method=='POST':
        form=formAstuce(data=request.POST)
        if form.is_valid():
            enregistrer=form.save()
            enregistrer.save()
            add_notifications(request.user , 'form', form)
            
        else:
            print(form.errors)
    else:
        form=formAstuce()


    content={
        'form':formAstuce,
    }

    return render(request,'astuces/formastuces.html',content)


@login_required
def homeastuce(request):
    return render(request,'astuces/acceuilleastuce.html')


@login_required
def voirAstuce(request):
    astuces=Astuce.objects.all()
    return render(request,'astuces/afficheastuce.html',{'astuce':astuces})