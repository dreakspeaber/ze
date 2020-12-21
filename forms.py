from django import forms
from web.models import *





class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'password'})) 
    


class HomeForm(forms.ModelForm):
    class Meta:
        model=Home
        fields='__all__'


class IntroForm(forms.ModelForm):
    class Meta:
        model=Intro
        fields='__all__'


class MethodForm(forms.ModelForm):
    class Meta:
        model=Methodology
        fields='__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'


class TeamForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'



class LinkForm(forms.ModelForm):
    class Meta:
        model=Links
        fields='__all__'

