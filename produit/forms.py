from django import forms
from .models import Vendeur,Produit,Demandeproduit




class demande(forms.ModelForm):
    nomproduit=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'le nom du produit'
        }
    ))
    prix=forms.CharField(widget=forms.NumberInput(
        attrs={
            'placeholder':'pour combien'
        }
    ))

    caractere=forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder':'decrire le produit ici'
        }
    ))
    numero=forms.CharField(widget=forms.NumberInput(
        attrs={
            'placeholder':'numero de telephone'
        }
    ))
    lieu=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'donner votre position'
        }
    ))

    class Meta:
        model=Demandeproduit
        fields=[
            'nomproduit',
            'caractere',
            'prix',
            'lieu',
            'numero',
        ]



    

class userVendeur(forms.ModelForm):
    user=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'le nom complet de vendeur '
        }
    ))
    specialite=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'veuille preciser votre travail ici'
        }
    ))
    ville=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'veuillez entrer la ville dans laquelle vous etes !'

        }
    ))
    number=forms.CharField(label='',widget=forms.NumberInput(
        attrs={
            'placeholder':'veuillez entrer votre numero de telephone '
        }
    ))
    class Meta:
        model=Vendeur
        fields=[
            'user',
            'specialite',
            'ville',
            'number',
        ]

class userProduit(forms.ModelForm):
    nom_produit=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'le nom du produit ici !'
        }
    ))
    caractere=forms.CharField(label='')
    typeproduit=forms.ChoiceField(label='',widget=forms.ChoiceField(
        
    ))
    prix=forms.CharField(label='',widget=forms.NumberInput(
        attrs={
            'placeholder':'le prix du produit'
        }
    ))
    applique=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'Decrivez l\'application du produit ici'
        }
    ))
    experiente=forms.DateField(label='',widget=forms.DateInput(
        attrs={
            'placeholder':'la date d\'experiention du produit '
        }
    ))
    
    class Meta:
        model=Produit
        fields=[
            'nom_produit',
            'caractere',
            'typeproduit',
            'prix',
            'applique',
            'experiente',
            
        ]