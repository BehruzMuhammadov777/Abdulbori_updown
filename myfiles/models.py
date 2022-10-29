from django.db import models

# Create your models here.

class Service(models.Model):
    nomi = models.CharField(max_length=50)
    manzil = models.CharField(max_length=70)
    eski_narxi = models.IntegerField()
    yangi_narxi = models.IntegerField()
    xonalar = models.IntegerField()
    yuvinish_xonasi = models.IntegerField()
    maydon = models.FloatField()
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)



class Clients(models.Model):
    ismi = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    malumot = models.CharField(max_length=800)
    lavozimi = models.CharField(max_length=300)
    rasmi = models.ImageField(upload_to='media')



class Agents(models.Model):
    ismi = models.CharField(max_length=50)
    fami = models.CharField(max_length=50)
    lavozimi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='media')


class Blogs(models.Model):
    nomi = models.CharField(max_length=50)
    maydoni = models.FloatField()
    malumot = models.CharField(max_length=800)
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)


class Murojat(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=800)
    subject = models.CharField(max_length=800)
    messege = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)