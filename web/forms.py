from django import forms

class StudentSignUpForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    department = forms.CharField()
    level = forms.CharField()
