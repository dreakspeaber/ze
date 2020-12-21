from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

def logoPath(self, filename):
    url = "self/%s" % (filename)
    return url

def galPath(self, filename):
    url = "self/gallery/%s" % (filename)
    return url


def ProfilePath(self, filename):
    url = "self/profile/%s" % (filename)
    return url

# Create your models here.
class Logo(models.Model):
    image=models.FileField(upload_to=logoPath) 


class Tm(models.Model):
    image=models.FileField(upload_to=logoPath) 


class Home(models.Model):
    caption = models.CharField(max_length=200)
    moto = models.CharField(max_length=300)
    image=models.FileField(upload_to=logoPath,blank=True) 
    mission = models.TextField()



class Intro(models.Model):
    caption = models.CharField(max_length=100)    
    image=models.FileField(upload_to=logoPath,blank=True) 
    text1 = models.TextField()
    text2 = models.TextField()
    head3 = models.CharField(max_length=64)
    text3 = models.TextField()
    head4 = models.CharField(max_length=64)
    text4 = models.TextField()
    head5 = models.CharField(max_length=64)
    text5 = models.TextField()
    text6 = models.TextField()
    

class Methodology(models.Model):
    caption = models.CharField(max_length=100)    
    image1=models.FileField(upload_to=logoPath,blank=True) 
    text1 = models.TextField()
    text2 = models.TextField()
    head3 = models.CharField(max_length=64)
    text3 = models.TextField()
    image3=models.FileField(upload_to=logoPath,blank=True) 
    head4 = models.CharField(max_length=64)
    text4 = models.TextField()
    image4=models.FileField(upload_to=logoPath,blank=True) 
    head5 = models.CharField(max_length=64)
    text5 = models.TextField()
    image5=models.FileField(upload_to=logoPath,blank=True) 


class Product(models.Model):
    head1 = models.CharField(max_length=64)
    text1 = models.TextField()
    image1 = models.FileField(upload_to=logoPath,blank=True) 
    head2 = models.CharField(max_length=64)
    text2 = models.TextField()
    image2 = models.FileField(upload_to=logoPath,blank=True) 
    head3 = models.CharField(max_length=64)
    text3 = models.TextField()
    image3 = models.FileField(upload_to=logoPath,blank=True) 
    head4 = models.CharField(max_length=64)
    text4 = models.TextField()
    image4 = models.FileField(upload_to=logoPath,blank=True) 
    head5 = models.CharField(max_length=64)
    text5 = models.TextField()
    image5=models.FileField(upload_to=logoPath,blank=True) 


class Gallery(models.Model):
    image = models.FileField(upload_to=galPath) 


class Callme(models.Model):
    name = models.CharField(max_length=100)    
    phone = models.CharField(max_length=100)    
    email = models.CharField(max_length=100)    
    interest = models.CharField(max_length=100)    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)    
    email = models.CharField(max_length=100)    
    message = models.TextField()   


class Employee(models.Model):
    name = models.CharField(max_length=100)    
    desg = models.CharField(max_length=100)    
    quali = models.CharField(max_length=100)
    image = models.FileField(upload_to=ProfilePath,blank=True) 
    twitter = models.CharField(max_length=400,blank=True,null=True,default='')
    facebook = models.CharField(max_length=400,blank=True,null=True,default='')



class Links(models.Model):
    facebook = models.URLField(blank=True,null=True,default='')
    insta  = models.URLField(blank=True,null=True,default='')
    twitter = models.URLField(blank=True,null=True,default='')
    linkd  = models.URLField(blank=True,null=True,default='')
