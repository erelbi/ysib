from django.db import models
import datetime
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

zaman = models.DateField()
zaman.contribute_to_class(User, 'zaman')

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Emir(models.Model):
    is_emri = models.CharField(max_length=100)
    tup_sayisi = models.CharField(max_length=100)
    baslangic = models.CharField(max_length=100)
    bitis = models.CharField(max_length=100)
    emri_veren = models.CharField(max_length=100)
