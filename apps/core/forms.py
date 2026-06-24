from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'input'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': INPUT_CLASSES}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES}))

class CrearcuentaForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': INPUT_CLASSES}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': INPUT_CLASSES}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES}))
