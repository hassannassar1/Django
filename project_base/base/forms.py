from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateProfileForm(UserCreationForm):
    username = forms.CharField(label='UserName',)
    first_name = forms.CharField(label='First Name',)
    last_name = forms.CharField(label='Last Name',)
    email = forms.EmailField(label='Email Address',)
    password1 = forms.CharField(label='Password',
                                    widget=forms.PasswordInput(),min_length=8)
    password2 = forms.CharField(label='Confirm Password',
                                    widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ('username','first_name','last_name',
                  'email','password1','password2')

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='User Name',)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='User Name',)
    email = forms.EmailField(label='Email Address',)
    password1 = forms.CharField(label='Password',
                                    widget=forms.PasswordInput(),min_length=8)
    password2 = forms.CharField(label='Confirm Password',
                                    widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('first_name','last_name','gender',
                  'bio','address','address_details',
                  'phone_number','image','slug',
                          )
