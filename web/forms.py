from django import forms

class StudentSignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    department = forms.CharField()
    level = forms.CharField()
