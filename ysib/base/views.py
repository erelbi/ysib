from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
        return render(request,'index.html')
@login_required
def arama(request):
        return render(request,'arama.html')
@login_required
def giriskalite(request):
        return render(request,'giris-kalite-kontrol.html')
@login_required
def isemri(request):
        return render(request,'is-emri.html')

#@login_required
def yetkilendirme(request):
        if request.method == 'POST':
                form = UserRegisterForm(request.POST)
                #profile_form = UserProfileInfoForm(data=request.POST)
                if form.is_valid(): #and profile_form.is_valid():
                        user = form.save()
                        user.refresh_from_db()
                        user.first_name = form.cleaned_data.get('first_name')
                        user.last_name = form.cleaned_data.get('last_name')
                        username = form.cleaned_data.get('username')
                        user.save()
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password1')
                        messages.success(request,f'{username} isimli kullanıcı eklendi!')
                        login(request, user)
                else:
                        print(form.errors)
        else:
                form = UserRegisterForm()
        return render(request,'kullanici-yetkilendirme.html',{'form':form})

@login_required
def performans(request):
        return render(request,'performans.html')
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
                





