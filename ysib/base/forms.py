from django import forms
#from django.contrib.auth import login , authenticate
from .models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Emir
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    first_name = forms.CharField(max_length=100, label='İsim')
    last_name = forms.CharField(max_length=100, label='Soyisim')
    zaman = forms.DateTimeField(initial=timezone.now())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1','password2','zaman')

class IsEmri(forms.ModelForm):
    is_emri = forms.CharField(max_length=100, label='İş Emri')
    tup_sayisi = forms.CharField(max_length=100, label='Tüp Sayısı')
    baslangic = forms.CharField(max_length=100, label='Başlangıç Zamanı')
    bitis = forms.CharField(max_length=100, label='Bitiş Zamanı')
    emri_veren = forms.CharField(max_length=100, label='Emri Veren')
    emir_zamani = forms.DateTimeField(initial=timezone.now())

    class Meta:
        model = Emir
        fields = ('is_emri', 'baslangic', 'bitis', 'tup_sayisi','emri_veren','emir_zamani')
