from django.contrib.auth import login
from django.contrib.auth.models import User 

from django.shortcuts import render, redirect 

from django.contrib.auth.decorators import login_required 

from .forms import StudentSignUpForm

from .models import Student

# Create your views here.
def home(request):
    return render(request, 'web/home.html')

def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            student = Student.objects.create(
                user=user,
                department=form.cleaned_data['department'],
                level=form.cleaned_data['level']
            )
            login(request, user)
            return redirect('home')  # Redirect after successful signup
    else:
        form = StudentSignUpForm()
    
    return render(request, 'web/signup.html', {'form': form})

@login_required
def dashboard(request):
    # Your view logic here
    return render(request, 'web/dashboard.html')
 