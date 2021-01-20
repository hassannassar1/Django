from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='أسم المستخدم',)
    first_name = forms.CharField(label='الأسم الأول',)
    last_name = forms.CharField(label='الأسم الأخير',)
    email = forms.EmailField(label='البريد الألكترونى',)
    password1 = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput(),min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور',widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')



class LoginForm(forms.ModelForm):
    username = forms.CharField(label='الأسم',)
    password = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
        
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='الأسم الأول',)
    last_name = forms.CharField(label='الأسم الأخير',)
    email = forms.EmailField(label='البريد الألكترونى',)

    class Meta:
        model = User
        fields = ('first_name','last_name','email',)
class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name','surname','subtitle',
                  'who_i','price','waiting_hours',
                  'working_hours','doctor',
                  'specialization','gender','address',
                  'address_details','phone_number','image',
                  'facebook','twitter','google',)



    