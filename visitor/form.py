from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class userforms(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':"nom d'utilisateur"
            }
        ))
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Votre prenom ',
        }
    ))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Votre nom de famille'
        }
    ))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'votre gmail'

        }
    ))

    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'nouveau mot de passe'
        }
    ))
    
    password2=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'confirmer le mot de passe'
        }
    ))
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
