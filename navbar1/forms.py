
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms





class UserCreation (UserCreationForm):
    class meta:
        model   =  User
        fields  = ['Username','first_name','last_name','password1','password2']
        # fields  = ('email')