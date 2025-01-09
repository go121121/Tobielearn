from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 
from pymongo import MongoClient 
import bcrypt

class SaveDataAws:
    def __init__(self): 
        pass 
    def hash_password(self,password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(),salt)
        return hashed_password.decode("utf-8")
    
    def check_password(self,password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode('utf-8'))  # Convert back to bytes for comparison
        