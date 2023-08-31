from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django import forms
from .models import PreferenceOption, Student, Room,Preference

class StudentSignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            if key != 'level':  # Exclude 'level' field
                field.label = ""
            
    username = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
    attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    department = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': 'Department'}))
    level = forms.ChoiceField(choices=Student.STUDENT_LEVEL,widget=forms.Select,label='Level')
    
  
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.label = ""
        
    username = UsernameField(widget=forms.TextInput(
    attrs={'placeholder': 'Username'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        }))
    
class RoomForm(forms.ModelForm):
    def __init__(self, *args,student=None, **kwargs):
        self.student=student
        super(RoomForm, self).__init__(*args, **kwargs)
                    
    room_type = forms.ChoiceField(choices=Room.ROOM_TYPES, required=True,widget=forms.Select, label="Room Type")
        
    room_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Room Address'}), label='Room Address')
        
    room_capacity = forms.IntegerField(widget=forms.NumberInput,label='Room Capacity')
        
    room_photo = forms.ImageField(widget=forms.FileInput,label='Room Photo')
    
    class Meta:
        model = Room
        fields = '__all__'
        
    # def save(self, commit=True, user=None):
    #     room = super().save(commit=False)
    #     if user:
    #         room.student = user
    #     if commit:
    #         room.save()
    #     return room

class PreferenceForm(forms.ModelForm):
    preferences = forms.ModelMultipleChoiceField(
        queryset=PreferenceOption.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Student  # Use the Student model, not Preference
        fields = ['preferences']

class PreferenceForm2(forms.Form):
    def __init__(self, *args, **kwargs):
        preferences = kwargs.pop('preferences')
        super(PreferenceForm2, self).__init__(*args, **kwargs)
        
        for preference in preferences:
            options = PreferenceOption.objects.filter(preference=preference)
            self.fields[f'preference_{preference.id}'] = forms.ModelChoiceField(queryset=options, label=preference.name)
    # preferences = forms.ModelMultipleChoiceField(
    #     queryset=PreferenceOption.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )

    class Meta:
        model = Student  # Use the Student model, not Preference
        fields = ['preferences']
