from django.urls import path
from .views import doctor_list,doctor_details,user_login,myprofile,signup,update_profile

app_name = 'accounts'
urlpatterns = [
        path('doctors/',doctor_list,name='doctor_list'),
        path('login/',user_login,name='login'),
        path('profile/',myprofile,name='profile'),
        path('signup/',signup,name='signup'),
        path('update_profile/',update_profile,name='update_profile'),
        path('<slug:slug>/',doctor_details,name='doctor_details'),
]