from django.shortcuts import render, redirect

from web.models import Student, User 
from .forms import StudentSignUpForm

# Create your views here.
def home(request):
    return render(request, 'web/home.html')

def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform other actions
            user = User(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            #save user and retrieve id
            #user.save()
            student = Student(user=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], department=form.cleaned_data['department'],level=form.cleaned_data['level'])
            student = Student(email=form.cleaned_data['email'],)
            #student.save()
            return redirect('home')  # Redirect after successful submission
    else:
        form = StudentSignUpForm()
    
    return render(request, 'roomiematch/home.html', {'form': form}) 

