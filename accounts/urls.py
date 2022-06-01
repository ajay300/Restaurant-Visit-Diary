from re import template
from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views as auth_views


from .forms import MyPasswordChangeForm

urlpatterns = [
    # Sign up & Login
    path('register/',views.ResgiterView.as_view() , name = 'register'),
    # path('login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html' , authentication_form = UserLoginForm), name = 'login'),
    path('login/',views.Userlogin, name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(next_page ='login') , name='logout'),

    # Password reset with email otp
    path('reset_password/',auth_views.PasswordResetView.as_view() , name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view() , name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view() , name='password_reset_complete'),

    # Change Password Without Otp.
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='accounts/passwordchange.html',form_class=MyPasswordChangeForm, success_url='passwordchangedone/'),name='passwordchange'),  
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/passwordchangedone.html'),name='passwordchangedone'),
]
