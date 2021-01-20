from django.urls import path
from .views import user_login,sign_up,update_profile,profile

app_name = 'base'
urlpatterns = [
        path('login/',user_login,name = 'login'),
        path('sign_up/',sign_up,name = 'sign_up'),
        path('update_profile/',update_profile,name = 'update_profile'),
        path('profile/',profile,name = 'profile'),
]
