from django.db import models
import datetime
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
zaman = models.DateField()
zaman.contribute_to_class(User, 'zaman')



class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Emir(models.Model):
    is_emri = models.CharField(max_length=100)
    tup_sayisi = models.CharField(max_length=100)
    urun_kodu = models.CharField(max_length=100)
    baslangic = models.DateField(default=timezone.now())
    bitis = models.DateField(default=timezone.now())
    emri_veren = models.CharField(max_length=100)
    emir_zamani = models.DateTimeField(default=timezone.now)

class Test(models.Model):
    tur = models.CharField(max_length=30)
    seri_no = models.CharField(max_length=20)
    acma = models.CharField(max_length=20)
    kapatma = models.CharField(max_length=20)
    testi_yapan = models.CharField(max_length=20)
    test_tarihi = models.DateTimeField(default=timezone.now,blank=True, null=True)

    def __str__(self):
        return self.seri_no
