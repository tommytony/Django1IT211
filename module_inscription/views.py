from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Create your views here.

def register_user(request):
    
    if request.method == 'POST':
        form= RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=user, password=password)
            login(request, user)
            messages.success(request, (" Vous êtes enregistrer avec success. "))
            return redirect('home')
    else:
        form=RegisterUserForm()
    
    return render(request,'inscription/register_user.html', {'form': form})



def login_user(request):
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return  redirect ('home')
            
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Erreur de connection, essayer à nouveau. ") )
            return  redirect ('login')
            pass
    else:
        
    
        return render(request, 'inscription/login.html', {}  )
    
 
def logout_user(request):
    logout(request)
    messages.success(request, (" Vous êtes déconnecter. ") )
    return redirect ('home')
    
