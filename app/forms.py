from socket import fromshare
# from xml.dom.minidom import Comment
from django import forms
from .models import  Chapter, ContactUs, Profile , CommentBox , Diary ,Restaurant
from django.forms.models import ModelForm
from django.contrib.auth.forms import AuthenticationForm , UsernameField , PasswordChangeForm
from django.utils.translation import gettext , gettext_lazy as _
# from django.contrib.auth.models import User
from accounts.models import User
from django.contrib.auth import password_validation
from django_countries.data import COUNTRIES

# Profile Form
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name','last_name','country']

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            
        }

# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','email','your_query']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'your_query':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }



# Diary Form
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title','diary_image','make_public']

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control'
            }),   

            'make_public':forms.CheckboxInput(attrs={
                'class':'form-check-input'
            }),
        }

# Chapter Form
class chapterform(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title' , 'diary']

        labels = {
            'title':'Title (not mendatory)'
        }

    # 'make_public':forms.BooleanField(attrs={
    #             'class':'form-check'
    #         }),

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','Location','dish','rating','review']

        labels = {
            'name':'Restaurant Name',
            'dish':'Favourite Dish',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter a name'}),
            'Loaction' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a Location'}),
            # 'chapter' : forms.CharField(attrs={'class':'form-control','placeholder':''}),
            'dish' : forms.TextInput(attrs={'class':'form-control','placeholder':'Favourite dish'}),
            # 'rating' : forms.TextInput(attrs={'class':'form-control'}),
            'review' : forms.TextInput(attrs={'class':'form-control','placeholder':'Write Something about hotel'}),
        }
            



# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBox
        fields = ['body']