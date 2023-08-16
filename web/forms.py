from django.contrib.auth.forms import AuthenticationForm,UsernameField

from django import forms


class StudentSignUpForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    department = forms.CharField()
    level = forms.CharField()
    
  
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
    
   
