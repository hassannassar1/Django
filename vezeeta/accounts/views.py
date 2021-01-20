from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import LoginForm,UserCreationForms,UpdateUserForm,UpdateProfileForm
# Create your views here.
def doctor_list(request):
    doctors = User.objects.all()
    context = {
                'doctors':doctors
            
            }
    return render(request,'user/doctors_list.html',context)

def doctor_details(request,slug):
    doctor_details = Profile.objects.get(slug=slug)
    context = {
                'doctor_details':doctor_details
            
            }
    return render(request,'user/doctor_details.html',context)

def user_login(request,):
    form =LoginForm()
    
    if request.method=='POST':
        form =LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts:doctor_list')
        else:
            form=LoginForm()
    context ={
            'form':form
            }
    return render(request,'user/login.html',context)
@login_required
def myprofile(request):
    context = {}
    return render(request,'user/myprofile.html',context)

def signup(request):
    form =UserCreationForms()
    if request.method=='POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('accounts:doctor_list')
        else:
            form = UserCreationForms()
    context = {
            'form':form
            }
    return render(request,'user/signup.html',context)


@login_required
def update_profile(request):
    user_form = UpdateUserForm(instance = request.user)
    profile_form = UpdateProfileForm(instance = request.user.profile)
    if request.method=='POST':
        user_form = UpdateUserForm(request.POST,instance = request.user)
        profile_form = UpdateUserForm(request.POST,request.FILES,instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:doctor_list')  
    else:
        user_form = UpdateUserForm(instance = request.user.profile)
        profile_form = UpdateProfileForm(instance = request.user.profile)
    context = {
            'user_form':user_form,
            'profile_form':profile_form
            }
    return render(request,'user/update_profile.html',context)

