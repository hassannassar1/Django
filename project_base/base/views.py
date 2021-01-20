from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CreateProfileForm, UpdateUserForm,UpdateProfileForm
# Create your views here.
def user_login(request,):
    form =LoginForm()
    
    if request.method=='POST':
        form =LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base:profile')
        else:
            form=LoginForm()
    context ={
            'form':form
            }
    return render(request,'profile/login.html',context)

def sign_up(request):
    form = CreateProfileForm()
    if request.method=='POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('base:profile')
        else:
            form = CreateProfileForm()
    context ={
            'form':form
            }
    return render(request,'profile/signup.html',context)
@login_required
def update_profile(request):
    user_form = UpdateUserForm(instance = request.user)
    profile_form = UpdateProfileForm(instance = request.user.profile)
    if request.method=='POST':
        user_form = UpdateUserForm(request.POST,instance = request.user)
        profile_form = UpdateUserForm(request.POST,request.FILES,
                                          instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('base:profile')  
    else:
        user_form = UpdateUserForm(instance = request.user.profile)
        profile_form = UpdateProfileForm(instance = request.user.profile)
    context = {
            'user_form':user_form,
            'profile_form':profile_form
            }
    return render(request,'profile/update_profile.html',context)

@login_required
def profile(request):
    context = {}
    return render(request,'profile/myprofile.html',context)
