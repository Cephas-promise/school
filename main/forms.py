
from dataclasses import fields
import imp
from django import forms
from django. contrib.auth import login, authenticate 
from django.contrib.auth. forms import UserCreationForm
from django.contrib.auth. models import User
from.models import Profile
class registerform(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    class Meta:
        model=User
        fields=['username','email','first_name', 'last_name', 'password1','password2']
       

class userupdateform(forms.ModelForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=40)
    last_name=forms.CharField(max_length=40)
    class Meta:
        model=User
        fields=['username','email','first_name', 'last_name']

class profileupdateform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image', 'MATRIC_NO', 'DEPARTMENT']



   