from django.contrib import admin

# Register your models here.
from .models import Student 
from .models import Room
from .models import Preference
from .models import PreferenceOption

admin.site.register(Student) 
admin.site.register(Room) 
admin.site.register(Preference) 
admin.site.register(PreferenceOption) 
