from .models import Astuce
from django import forms

class formAstuce(forms.ModelForm):
    titre=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'un titre à l\'astuce'
        }
    ))
    astuce=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'Decrire ici votr astuce'
        }
    ))
    media=forms.FileField(label='',widget=forms.FileInput(
        attrs={
            'placeholder':'deposer ici fichier/video/image concernat l\'astuce'
        }
    ))
    

    class Meta:
        model=Astuce
        fields=[
            'titre',
            'astuce',
            'media',
            
        ]