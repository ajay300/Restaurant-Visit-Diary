from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views as auth_views
# from .forms import UserLoginForm
# from .forms import MyPasswordChangeForm, UserLoginForm

urlpatterns = [

    path('',views.home , name = 'home'),
    path('profile-form/',views.ProfileFormView.as_view() , name = "profile-form"),
    path('profile/<int:pk>/',views.ProfileView , name = 'profile'),
    path('dashboard/',views.Dashboard , name = "dashboard"),
    path('profile/<str:pk>/',views.profielUser , name = 'profiles'),
  
    # Diary
    path('add-diary/',views.AddDiary.as_view() , name = "add-diary"),
    path('update-diary/<int:pk>/',views.UpdateDiary , name = "update-diary"),
    path('delete-diary/<int:pk>/',views.DeleteDiary , name = 'delete'),

    # ChapterView
    path('diary-detail/<int:pk>/',views.ChapterView.as_view() , name = "diary-detail"),
    path('add-chapter/',views.AddChapter.as_view() , name = 'add-chapter'),
    path('delete-chapter/<int:pk>/',views.deleteChapter , name = "delete-chapter"),
    
    #restaurantView
    path('resto-detail/<int:pk>/',views.RestaurantView.as_view() , name = "resto-detail"),
    # path('resto-form/',views.RestaurantFormView.as_view() , name = 'resto-form'),
    path('resto-form/<int:pk>/',views.restaurantForm , name = 'resto-form'),

    # Contact US
    path('contact/',views.ContactFormView.as_view() , name = 'contact')


    

    

    # # Password Change 
    # path('account/passwordchange/',auth_views.PasswordChangeView.as_view(
    #     template_name= 'app/passwordchange.html' , form_class=MyPasswordChangeForm), name='passwordchange'),
        
    # path('account/passwordchangedone/',auth_views.PasswordChangeView.as_view(
    #     template_name= 'app/passwordchange.html'), name='passwordchangedone'),
    


    
    
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

