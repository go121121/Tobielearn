from django.shortcuts import render,redirect 
from .forms import CustomUserForm
from django.contrib.auth import login as auth_login, authenticate
from .backen import Mybackend
from django.template import loader 
import json 
from .models import CustomUser,Address 
from django.http import JsonResponse

# Create your views here.
def register(request): 
        if request.method=="POST":  
                form=CustomUserForm(request.POST)
                
                if form.is_valid(): 
                    user=form.save()
                    login(request,user)
                    return redirect('login')
                    
                else: 
                    return render(request,"registration.html",{"form":form})
        else: 
            form=CustomUserForm()
        
        return render(request,"registration.html",{"form":form})
    
def login(request): 
    Usermodel=Mybackend()
    if request.method=="POST": 
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=Usermodel.login_check(username=username,password=password) 
        if user is not None : 
            request.session['username']=username 
            return redirect("learn")
        else: 
            form=CustomUserForm(request.POST)
    else: 
       form=CustomUserForm()
    return render(request,"login.html",{"form":form})

def learn_page(request): 
    return render(request,"learn_page.html")


def save_address(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extract and validate fields
            address1 = data.get('address1')
            address2 = data.get('address2', '')
            state = data.get('state')
            postal = data.get('postal')
            
            if not address1 or not state or not postal:
                return JsonResponse({'success': False, 'message': 'All required fields must be filled in.'}, status=400)
            
            # Get the user from the session
            username = request.session.get('username')
            if not username:
                return JsonResponse({'success': False, 'message': 'User not logged in.'}, status=403)
            
            user = CustomUser.objects.get(username=username)
            
            # Create or update the address
            address, created = Address.objects.get_or_create(
                address1=address1, address2=address2, state=state, postal=postal
            )
            request.session['address']=address 
            
            # Assign the address to the user and save
            user.address = address
            user.save()
            
            return JsonResponse({"success": True, 'message': "Address saved successfully!"})
        
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid data format.'}, status=400)
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found.'}, status=404)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

    
        

def home(request): 
    Username=request.session.get('username')
    initial_address=None 
    if request.method=="POST": 
        save_address(request)
        initial_address=request.session.get('address')
    else:
        initial_address= "Your Location"
    context={
        "username":Username, 
        'address':initial_address
    }
    return render(request,"home.html",context)
    
        
        
    
    

            