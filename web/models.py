from django.contrib.auth.models import User 
from django.conf import settings
from django.db import models


class Preference(models.Model):
    name = models.CharField(max_length=100,  default="None")  # E.g., "Gender", "Religion", etc.

    def __str__(self):
        return self.name


class PreferenceOption(models.Model):
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)

    def __str__(self):
        return self.option

class Student(models.Model):
    STUDENT_LEVEL = [
        ('100', 'Year One'),
        ('200', 'Year Two'),
        ('300', 'Year Three'),
        ('400', 'Post Graduate'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    level = models.IntegerField(choices=STUDENT_LEVEL)
    preferences = models.ManyToManyField(PreferenceOption)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
        ('other', 'Other'),
    ]
    ROOM_STATUS=[
        ('available','Available'),
        ('not available','Not Available')
    ]
    room_type = models.CharField(max_length=50,choices=ROOM_TYPES)
    room_address = models.CharField(max_length=200)
    room_status = models.CharField(max_length=20,choices=ROOM_STATUS)
    room_capacity = models.IntegerField()
    room_photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)

class Match(models.Model):
    match_student = models.ForeignKey(Student, related_name='match_student', on_delete=models.CASCADE)
    match_to_student = models.ForeignKey(Student, related_name='match_to_student', on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    MATCH_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    match_status = models.CharField(max_length=10, choices=MATCH_STATUS_CHOICES)

class Message(models.Model):
    message = models.TextField()
    status = models.CharField(max_length=20)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
