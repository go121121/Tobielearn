from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import CustomUser 

class CustomUserForm(AuthenticationForm):
    username = forms.CharField(label=' Email',
                               max_length=250,
                               )
    password = forms.CharField(widget=forms.PasswordInput)
        
    
    class Meta: 
        model=CustomUser 
        fields=['username','password']
        