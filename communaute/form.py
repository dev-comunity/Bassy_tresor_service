from django import forms
from .models import*

class Formreve(forms.ModelForm):

    decrire=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'veuillez expliquer le reve ici !'
        }
    ))
    adress=forms.EmailField(label='',widget=forms.EmailInput(
        attrs={
            'placeholder':'votre E-mail !'
        }
    ))
    numero=forms.CharField(label='',widget=forms.NumberInput(
        attrs={
            'placeholder':'votre de telephone facultatif'
        }
    ))

    class Meta:
        model=DemandeReve
        fields=[
            #'nom',
            #'datereve',
            'decrire',
            'adress',
            'numero',
        ]


class DeposReve(forms.ModelForm):
    objet=forms.CharField(widget=forms.TextInput(
        attrs={
            'Placeholder':'Le but du reve '
        }
    ))

    desc=forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder':'Exppliquez le reve ici !'
        }
    ))

    class Meta:
        model=Reve
        fields=[
            "objet",
            'desc'
        ]