from django import forms
#from django.contrib.auth import login , authenticate
from .models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Emir, User ,Test
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
#kendi alanımız oluşturabiliyoruz:)
class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    first_name = forms.CharField(max_length=100, label='İsim')
    last_name = forms.CharField(max_length=100, label='Soyisim')
    zaman = forms.DateTimeField(initial=timezone.now)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1','password2','zaman')

class IsEmri(forms.ModelForm):
    is_emri = forms.CharField(max_length=100, label='İş Emri')
    tup_sayisi = forms.CharField(max_length=100, label='Tüp Sayısı')
    urun_kodu = forms.CharField(max_length=100, label='Ürün Kodu')
    baslangic = forms.DateInput()
    bitis = forms.DateInput()
    emri_veren = forms.CharField(label='Emri Veren')
    emir_zamani = forms.DateTimeField(initial=timezone.now())

    class Meta:
        model = Emir
        widgets = {
            'baslangic': DateInput(),
            'bitis': DateInput(),
        }
        fields = ('is_emri', 'baslangic', 'bitis', 'tup_sayisi','emri_veren','emir_zamani')


class TestForm(forms.ModelForm):
    tur = forms.CharField(max_length=100)
    seri_no = forms.CharField(max_length=100)
    acma = forms.CharField(max_length=100)
    kapatma = forms.CharField(max_length=100)
    testi_yapan = forms.CharField()
    text_tarihi = forms.DateTimeField(initial=timezone.now)

    class Meta:
        model = Emir
        fields = ('tur', 'seri_no', 'acma', 'kapatma','text_tarihi')
