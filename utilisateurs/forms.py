from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utlisateur", widget=forms.TextInput(
        attrs={
                "class":"form-control",
                "placeholder":"Username"

        }
    ))
    password =forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={
                "class":"form-control",
                "placeholder":"Password"
        }
    ))


class SignUpForm(UserCreationForm):

    username = forms.CharField(label="Nom d'utlisateur", widget=forms.TextInput(
        attrs={
                "class":"form-control",
                "placeholder":"username"

        }
    ))

    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={
                "class":"form-control",
                "placeholder":"votre address mail"

        }
    ))

    password1 =forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={
                "class":"form-control",
                "placeholder":"Password"

        }
    ))

    password2 =forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput(
            attrs={
                    "class":"form-control",
                    "placeholder":"Confirm Password"

            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
