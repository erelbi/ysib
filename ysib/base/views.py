from django.shortcuts import render,redirect
from .forms import UserRegisterForm, IsEmri ,TestForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Emir , Test
from django.contrib.auth.decorators import login_required
import platform
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
mac = platform.machine()[:3] # eğer device ras pi ise 'arm' döner
@login_required
def index(request):
        return render(request,'index.html', { 'mac' : mac })
@login_required
def arama(request):
        testler = Test.objects.all()
        return render(request,'arama.html',{ 'mac' : mac , 'testler' : testler})
@login_required
@csrf_exempt
def giriskalite(request):
        #Test.objects.all().delete()  Test sonuçlarını silmek için 
        fullname = request.user.first_name + ' ' + request.user.last_name
        if request.method == 'POST':
                if request.POST.dict()['tur'] == 'basinc':
                        veris = json.loads(request.POST.dict()['veri'])
                        for veri in veris:
                                t = Test(tur='basinc',seri_no = veri[0] , acma = veri[1] , kapatma = veri[2] ,testi_yapan = fullname)
                                t.save(force_insert=True)
                elif request.POST.dict()['tur'] == 'emniyet':
                        veri = request.POST.dict()['veri']
                        print(veri)
        return render(request,'giris-kalite-kontrol.html',{ 'mac' : mac })
@login_required
@csrf_exempt
def uretimkontrol(request):
        #Test.objects.all().delete()  #Test sonuçlarını silmek için bu yorumu açabilirsiniz abi
        fullname = request.user.first_name + ' ' + request.user.last_name
        if request.method == 'POST':
                if request.POST.dict()['tur'] == 'Valf Montaj':
                        veris = json.loads(request.POST.dict()['veri'])
                        for veri in veris:
                                t = Test(tur='Valf Montaj',seri_no = veri[0] , acma = veri[1] , kapatma = veri[2] ,testi_yapan = fullname)
                                t.save(force_insert=True)
        return render(request,'uretim-kontrol.html',{ 'mac' : mac })
@login_required
def isemri(request):
        fullname = request.user.first_name + ' ' + request.user.last_name
        emirler = Emir.objects.all()
        if request.method == 'POST':
                form = IsEmri(request.POST)
                if form.is_valid():
                        emir = form.save()
                        emir.refresh_from_db()
                        emir.is_emri = form.cleaned_data.get('is_emri')
                        emir.urun_kodu = form.cleaned_data.get('urun_kodu')
                        emir.baslangic = form.cleaned_data.get('baslangic')
                        emir.bitis = form.cleaned_data.get('bitis')
                        emir.emri_veren = form.cleaned_data.get('emri_veren')
                        messages.success(request,'{} isimli kullanıcı tarafından bir emir eklendi!'.format(emir.emri_veren))
                        emir.save()
                        form.full_clean()
        else:
                form = IsEmri()
                form.fields["emri_veren"].initial = fullname
        return render(request,'is-emri.html', { 'form' : form , 'emirler': emirler , 'mac' : mac , 'fullname' : fullname })

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
                        messages.success(request,'{} isimli kullanıcı eklendi!'.format(username))
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
def yazdir(request):
        return render(request,'yazdir.html',{ 'mac' : mac })
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
                                print('{} kullanıcısı tarafından başarılı giriş'.format(username))
                                return redirect('index')
                        else:
                                messages.warning(request,'Kullanıcı adınızı yada parolanızı yanlış girdiniz.')
                else:
                        print("Birisi login olmayı denedi ve başarısız oldu!")
                        messages.warning(request,'Kullanıcı adınızı yada parolanızı yanlış girdiniz.')
                        return redirect('index')
        else:
                return render(request,'login.html',{})
                





