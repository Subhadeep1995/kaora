
from django import forms
from django.forms import extras
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


