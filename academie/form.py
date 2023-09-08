from .models import Academiecours,Academicien,Questionnaire,Adhesion

from django import forms
from django.contrib.auth.forms import UserCreationForm




class questions(forms.ModelForm):
    question=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'poser votre question ici',
            'row':10,
            'colm':15
        }
    ))
    class Meta:
        model=Questionnaire
        fields=[
            'question'
        ]


class formAcademicien(forms.ModelForm):
    nom=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'votre nom complet ici '
        }
    ))
    age=forms.DateField(widget=forms.DateInput(
        attrs={
            'placeholder':'votre Age'

        }
    ))

    ville=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'la ville où vous habitez actuellement'
        }
    ))
    
    class Meta:
        model=Academicien
        fields=[
            'nom',
            'age',
            'ville',
            'modeapprend',
        ]


class formAcademiecours(forms.ModelForm):
    titre=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'le titre du cours facultatif'
        }
    ))
    image_cours=forms.ImageField(label='',widget=forms.FileInput(
        attrs={
            'placeholder':'une image du cours facultatif'
        }
    ))

    deposer_lesson=forms.FileField(label='',widget=forms.FileInput(
        attrs={
            'placeholder':'deposer un fichier du cours facultatif'
        }
    ))
    ecrire_lesson=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'Saisissez la leçon ici !'
        }
    ))

    class Meta:
        model=Academiecours
        fields=[
            'titre',
            'image_cours',
            'deposer_lesson',
            'ecrire_lesson',
        ]

class formAdhesion(forms.ModelForm):
    #nom=forms.CharField(widget=forms.TextInput(
       # attrs={
      #      'placeholder':'Veuillez saisir votre nom !'
     #   }
    #))
    #prenom=forms.CharField(widget=forms.TextInput(
       # attrs={
      #      'placeholder':'Veuillez saisir votre prenom !'
     #   }
    #))
    objet=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Veuillez saisir l\'objet de la demande !'
        }
    ))
    demande=forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder':'Veuillez saisir votre demande ici !',
            'row':15,
            'colm':5

        }
    ))
    
    adresse=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Veuillez saisir votre adresse E-mail !'
        }
    ))
    numero=forms.CharField(widget=forms.NumberInput(
        attrs={
            'placeholder':'Veuillez entrer votre numero de telephone !'
        }
    ))
    class Meta:
        model=Adhesion
        fields=[
            #'nom',
            #'prenom',
            'objet',
            'demande',
            'mode',
            'adresse',
            'numero',
        ]
