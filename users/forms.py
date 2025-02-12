from django import forms
from django.forms import ModelForm, DateInput

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User



#  A form for the input required for the commenting functionality.

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        labels = {'username' : 'Enter Username', 'email' : 'Enter Email','password1' : 'Enter Password', 'password2' : 'Re-Enter Password'}


class LoginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username', 'password']
        labels = {'username' : 'Enter Username', 'password' : 'Enter Password'}
        