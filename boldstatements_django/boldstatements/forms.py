from django import forms
from .models import Statement, User
from django.forms import CharField, PasswordInput

class MakeAStatement(forms.ModelForm):

    class Meta:
        model = Statement
        fields = ('prediction', 'predictor', 'description', 'image', 'link')

class LoginForm(forms.ModelForm):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class UserCreationForm(forms.ModelForm):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())
    firstname = CharField(max_length=100)
    lastname = CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'password', 'firstname', 'lastname')
