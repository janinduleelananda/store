from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email=forms.EmailField(max_length=200,help_text='eg. name@anymail.com')

    class Meta:
        model = User
        fields=('first_name','last_name','username','password1','password2')
class signinform(AuthenticationForm):
    class Meta:
        model =User
        fields = ('username','password')