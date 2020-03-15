from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request,'index.html')

def arama(request):
        return render(request,'arama.html')

def giriskalite(request):
        return render(request,'giris-kalite-kontrol.html')

def isemri(request):
        return render(request,'is-emri.html')

def yetkilendirme(request):
        return render(request,'kullanici-yetkilendirme.html')

def login(request):
        return render(request,'login.html')

def performans(request):
        return render(request,'performans.html')