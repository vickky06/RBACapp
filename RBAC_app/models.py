#from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _
import datetime



class User(models.Model):
    username = models.CharField(max_length=100,unique=True)
    user_id = models.CharField(max_length=5,unique=True)
    mail_id = models.EmailField(unique=True)



class wareHouse(models.Model):
    claims = models.CharField(max_length = 250,blank=True)
    description =  models.CharField(max_length = 2500,blank=True)
    addDate = models.DateField(blank=True,auto_now=True)
    assigne =  models.CharField(max_length = 150,blank=True)
    document = models.FileField(upload_to='documents/')
    

    
    #accessLevel = models.IntegerField(default =0,validators=[MinValueValidator(0), MaxValueValidator(3)])

class SessionAudit(models.Model):
    username = models.CharField(max_length=100)
    keywordsAudit = models.CharField(max_length=5000) 
    date = models.DateField(auto_now_add=True)

      



    #accessLevel = models.IntegerField(default =0,validators=[MinValueValidator(0), MaxValueValidator(3)])


