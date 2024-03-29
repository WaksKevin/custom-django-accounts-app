from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
    UsernameField,
)

from .models import User

class LoginForm(AuthenticationForm):
    email = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Your email",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Your password",
            }
        ),
    )
