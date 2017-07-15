from django import forms
from .models import *


class SignupForm(forms.Form):

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "correo@gmail.com"
            }
        )
    )

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "nombre"
            }
        )
    )

    apaterno = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Apellido"
            }
        )
    )

    descripcion = forms.CharField(
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "descripcion"
            }
        )
    )
    GENDER_CHOICES = (
        ('M', 'Mujer'),
        ('H', 'Hombre')
    )
    genero = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "descripcion"
            },  
            choices=GENDER_CHOICES
        )
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password"
            }
        )
    )
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "confirm password"
            }
        )
    )


def clean(self):
    cleaned_data = super(SignupForm, self).clean()
    pasword = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")
    if password != confirm_password:
        raise forms.ValidationError(
            "password and confirm password must be the same (they are not right now...)!"
        )


class LoginForm(forms.Form):

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "correo@gmail.com"
            }
        )
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password"
            }
        )
    )
