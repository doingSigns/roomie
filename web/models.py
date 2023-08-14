from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
'''
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=20)
'''

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    level = models.IntegerField()

class Room(models.Model):
    room_type = models.CharField(max_length=50)
    room_address = models.CharField(max_length=200)
    room_status = models.CharField(max_length=20)
    room_capacity = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)

class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferences = models.TextField()  #Might still need to define the structure of preferences here

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
