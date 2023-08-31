import pprint
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist 

from django.shortcuts import render,get_object_or_404, redirect 

from django.contrib.auth.decorators import login_required 

from django.core.exceptions import ValidationError 

from .models import Student, Preference, PreferenceOption, Match,Room

from .forms import StudentSignUpForm 
from .forms import RoomForm 
from .forms import PreferenceForm

from .matching_algorithm import get_matched_students

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('web:dashboard')
    
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
def room_list(request):
    student = request.user.student
    rooms = Room.objects.filter(student=student)
    return render(request, 'web/room_list.html', {'rooms': rooms})

@login_required
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'web/room_detail.html', {'room': room})

@login_required
def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST,request.FILES)
        if form.is_valid():
            student_instance = Student.objects.get_or_create(user=request.user)[0]
            room= Room(
                room_type=form.cleaned_data['room_type'],
                room_address=form.cleaned_data['room_address'],
                room_capacity=form.cleaned_data['room_capacity'],
                room_photo=form.cleaned_data['room_photo'],
                student=student_instance
            )
            room.save()
            # form.save()
            return redirect('web:room_list')
    else:
        form = RoomForm()
    
    return render(request, 'web/rooms_form.html', {'form': form})

@login_required
def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('web:room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'web/rooms_form.html', {'form': form})

@login_required
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('web:room_list')
    return render(request, 'web/room_confirm_delete.html', {'room': room})

@login_required
def dashboard(request):
    user = request.user

    try:
        student = Student.objects.get(user=user)
        if student.preferences.exists():
            # Render the dashboard with the user's preferences
            preferences = student.preferences.all()

            #Fetch existing matches for the student 
            matches = Match.objects.filter(match_student=student) 

            available_rooms = {}

            for match in matches:
                # Retrieve the corresponding room for the match
                room = Room.objects.filter(student=match.match_to_student, room_status='available').first()
                if room: 
                    # Add the matched student as the key and the room as the value to the dictionary
                    available_rooms[match.match_to_student] = room

            return render(request, 'web/dashboard.html', {'preferences': preferences, 'student': student, 'matches': matches, 'available_rooms': available_rooms})
        
        else:
            # Redirect to the preference form
            return redirect('web:preference_form')
    except Student.DoesNotExist:
        # Redirect to the preference form
        return redirect('web:preference_form')

@login_required
def preference_form(request):
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = PreferenceForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # Save the student instance along with the selected preferences
            return redirect('web:dashboard')  # Redirect to dashboard after saving preferences
    else:
        form = PreferenceForm(instance=student)

# We trigger the Gale-Shapely algorithm to generate matches 
    matches = get_matched_students()

    return render(request, 'web/preference_form.html', {'form': form})


def matches(request):

# We trigger the Gale-Shapely algorithm to generate the matches 
    matches = get_matched_students()
    
    return render(request, 'web/matches.html', {'matches': matches})
