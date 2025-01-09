from django.contrib.auth.backends import BaseBackend
from .data import SaveDataAws
from .models import CustomUser

class Mybackend(BaseBackend): 
    
    def authenticate(self,request, username =None, password =None):
        try: 
            UserModel = CustomUser
            user = UserModel.objects.get(username=username) 
            if SaveDataAws.check_password(self,password,hashed_password=user.password): 
                    return user
            else: 
                return None 
        except UserModel.DoesNotExist: 
            if username and password: 
                user=UserModel(username=username)
                new_password=SaveDataAws.hash_password(self,password=password)
                if SaveDataAws.check_password(self,password,new_password): 
                    user.password=new_password
                    user.save()
                    return user 
                return None 
    def login_check(self,username=None,password=None):
            UserModel = CustomUser
            user = UserModel.objects.get(username=username) 
            if SaveDataAws.check_password(self,password,hashed_password=user.password): 
                    return user
            else: 
                return None 
         
        
                
                