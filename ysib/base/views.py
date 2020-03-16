from django.shortcuts import render
from .forms import RegisterForm

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
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request,'kullanici-yetkilendirme.html',{"form":form})


def performans(request):
        return render(request,'performans.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request,"register.html",{"form":form})