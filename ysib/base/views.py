from django.shortcuts import render,redirect
from .forms import UserRegisterForm, IsEmri
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Emir
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
#kullanicilar = User.objects.all()
#emirler = Emir.objects.all()
mac = os.uname()[4][:3] # eğer device res pi ise 'arm' döner
@login_required
def index(request):
        return render(request,'index.html', { 'mac' : mac })
@login_required
def arama(request):
        return render(request,'arama.html',{ 'mac' : mac })
@login_required
def giriskalite(request):
        return render(request,'giris-kalite-kontrol.html',{ 'mac' : mac })
@login_required
def uretimkontrol(request):
        return render(request,'uretim-kontrol.html',{ 'mac' : mac })
@login_required
def isemri(request):
        emirler = Emir.objects.all()
        if request.method == 'POST':
                form = IsEmri(request.POST)
                if form.is_valid():
                        emir = form.save()
                        emir.refresh_from_db()
                        emir.is_emri = form.cleaned_data.get('is_emri')
                        emir.baslangic = form.cleaned_data.get('baslangic')
                        emir.bitis = form.cleaned_data.get('bitis')
                        emir.emri_veren = form.cleaned_data.get('emri_veren')
                        messages.success(request,f'{emir.emri_veren} isimli kullanıcı tarafından bir emir eklendi!')
                        emir.save()
                        form.full_clean()
        else:
                form = IsEmri()
        return render(request,'is-emri.html', { 'form' : form , 'emirler': emirler , 'mac' : mac})

#@login_required
def yetkilendirme(request):
        kullanicilar = User.objects.all()
        if request.method == 'POST':
                form = UserRegisterForm(request.POST)
                if form.is_valid(): #and profile_form.is_valid():
                        user = form.save()
                        user.refresh_from_db()
                        user.first_name = form.cleaned_data.get('first_name')
                        user.last_name = form.cleaned_data.get('last_name')
                        user.save()
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password1')
                        messages.success(request,f'{username} isimli kullanıcı eklendi!')
                        login(request, user)
                else:
                        print(form.errors)
        else:
                form = UserRegisterForm()
        return render(request,'kullanici-yetkilendirme.html',{'form':form,'kullanicilar':kullanicilar , 'mac' : mac})

@login_required
def performans(request):
        return render(request,'performans.html',{ 'mac' : mac })
@login_required
def ulogout(request):
        logout(request)
        return(HttpResponseRedirect(reverse('ulogin')))

def ulogin(request):
        if request.method == 'POST':
                #birim = request.POST.get('birim')
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username,password=password)
                if user:
                        if user.is_active:
                                login(request,user)
                                print(f'{username} kullanıcısı tarafından başarılı giriş')
                                return redirect('index')
                        else:
                                messages.warning(request,'Kullanıcı adınızı yada parolanızı yanlış girdiniz.')
                else:
                        print("Birisi login olmayı denedi ve başarısız oldu!")
                        messages.warning(request,'Kullanıcı adınızı yada parolanızı yanlış girdiniz.')
                        return redirect('index')
        else:
                return render(request,'login.html',{})
                





