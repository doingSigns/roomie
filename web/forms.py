from django.contrib.auth.forms import AuthenticationForm,UsernameField

from django import forms


class StudentSignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
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
    level = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': 'Level'}))
    
  
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
    
   
