from django import forms
#from django.contrib.auth import login , authenticate
#from .models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    first_name = forms.CharField(max_length=100, label='İsim')
    last_name = forms.CharField(max_length=100, label='Soyisim')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1','password2')

