from django.contrib.auth import login
from django.contrib.auth.models import User 

from django.shortcuts import render, redirect 

from django.contrib.auth.decorators import login_required 

from django.core.exceptions import ValidationError 

from .forms import StudentSignUpForm

from .models import Student

# Create your views here.
def home(request):
    form = StudentSignUpForm() 
    return render(request, 'web/home.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            # Check if a user with the provided username or email already exists
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'A user with this username already exists.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'A user with this email already exists.')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=email,
                    password=form.cleaned_data['password']
                )
                student = Student.objects.create(
                    user=user,
                    department=form.cleaned_data['department'],
                    level=form.cleaned_data['level']
                )
                login(request, user)
                return redirect('web:dashboard')  # Redirect after successful signup
    else:
        form = StudentSignUpForm()
    
    return render(request, 'web/signup.html', {'form': form})

@login_required
def dashboard(request):
    # Your view logic here
    return render(request, 'web/dashboard.html')
 