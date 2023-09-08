from django import forms
from .models import Consultation,Reponse



class formconsultation(forms.ModelForm):

    nom=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'veuillez entrer le nom de consultant'
        }
    ))
    objet=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'veuillez saisir l\'objet !'
        }
    ))

    Description=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'veuillez expliquer pour quoi consulter ici !'
        }
    ))
    

    numero=forms.CharField(widget=forms.NumberInput(
        attrs={
            'placeholder':'telephone'
        }
    ))

    adress=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'E-mail ici'
        }
    ))
    class Meta:
        model=Consultation
        fields=[
           'nom',
            'objet',
            'Description',
            'mode',
            'numero',
            'adress',
        ]

class Formreponse(forms.ModelForm):
    nom=forms.CharField(label='Nom de consultant',widget=forms.TextInput(
        attrs={
            'placeholder':'veuillez entrer le nom de consultant'
        }
    ))

    son_but=forms.CharField(label='la raison de sa consultation',widget=forms.TextInput(
        attrs={
            'placeholder':'ici le but de sa consultation'
        }
    ))
    desc=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'decrivez le resultat de sa consultation ici !'
        }
    ))

    class Meta:
        model=Reponse
        fields=[
            'nom',
            'son_but',
            'desc',
        ]