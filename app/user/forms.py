from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': 'autofocus'}))
    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
