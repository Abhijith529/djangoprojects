from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import CustomUser
from django.forms.fields import ChoiceField


class Signupform(UserCreationForm):
    role_choices=(('student','Student'),('teacher','Teacher'))
    role=ChoiceField(choices=role_choices)
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','role','phone']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
