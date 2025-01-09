from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Address(models.Model): 
   address1=models.CharField(max_length=255)
   address2=models.CharField(max_length=255,blank=True,null=True)
   state=models.CharField(max_length=100)
   postal=models.CharField(max_length=20)
   
class Profile(models.Model): 
   user=models.OneToOneField('CustomUser', on_delete=models.CASCADE)
   bio=models.TextField(blank=True)
   birth_date=models.DateField(null=True,blank=True)
   phone_number=models.CharField(max_length=15,blank=True)

class CustomUser(AbstractUser):
     username=models.CharField(unique=True,blank=False,max_length=255)
     address=models.ForeignKey(Address, on_delete=models.CASCADE, null=True,blank=True)
     phone_number = models.CharField(max_length=15, blank=True)  # Allow optional phone numbers
     

