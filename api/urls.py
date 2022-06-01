from django.contrib import admin
from django.urls import path
from . import views
# from accounts.views import UserRegistrationView
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import SendPasswordResetEmailView , UserChangePasswordView ,UserPasswordResetView, UserProfileView



urlpatterns = [
    # JWT AUTHENTICATION
    path('register/',views.UserRegistrationView.as_view() , name = 'api-register'),
    path('login/',views.UserLoginView.as_view() , name = 'api-login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),


    #Combo Concrete View
    path('contactview/',views.ContactListcreate.as_view()),
    path('contactadd/<int:pk>/',views.ContactRetrieveUpdate.as_view()),
    path('contactapiremove/<int:pk>',views.ContactRetrieveDestroy.as_view()),
        
]



