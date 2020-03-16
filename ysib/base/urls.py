from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('arama', views.arama, name='arama'),
    path('giriskalite', views.giriskalite, name='giriskalite'),
    path('isemri', views.isemri, name='isemri'),
    path('yetkilendirme', views.yetkilendirme, name='yetkilendirme'),
    path('performans', views.performans, name='performans'),
    path('register/', views.register, name='register'),
    #path('login', views.loginpage, name='loginpage'),
    #path('profile/', views.profile, name='profile'),
    #path('logout/', views.logout, name='logout'),
]
