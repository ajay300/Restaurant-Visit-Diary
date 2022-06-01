from django import forms
from django.forms.models import ModelForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm , UsernameField , PasswordChangeForm
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control ','placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        }


# Login Form
# class UserLoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={'placeholder':'Enter a Username' , 'class':'form-control'}))
#     password = forms.CharField(
#         label=('Password') ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'placeholder':'Enter a password','class':'form-control'})
#     )

# Password Change Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old_Password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-password' , 'class':'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'),widget=forms.PasswordInput(attrs={'autocomplete':'new-password' , 'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm Password'),widget=forms.PasswordInput(attrs={'autocomplete':'confirm-password' , 'class':'form-control'}))



class ForgetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['email']

# class MyPasswordChangeForm()