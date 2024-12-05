from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Snack


def home(request):
    snacks = Snack.objects.all()  # Get all snacks from the database
    return render(request, 'home.html', {'snacks': snacks})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Create user manually
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            # Log the user in after registration
            login(request, user)
            return redirect('home')  # Redirect to home after successful registration
        except:
            messages.error(request, "Error in registration. Please try again.")
            return redirect('register')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')






def user_logout(request):
    logout(request)
    return redirect('login')