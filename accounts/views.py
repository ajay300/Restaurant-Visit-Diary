from django.shortcuts import render ,redirect
from django.contrib.auth import login 
from .forms import ForgetPasswordForm, RegistrationForm 
from django.contrib import messages
from .models import User
from django.views import View


# Create your views here.

# AUthentications.
class ResgiterView(View):
    def get(self,request):

        # if request.user.is_authenticated:  #if user is already logged in so it redirect to home except login page again 
        #     return redirect('home')

        form = RegistrationForm()
        return render(request , 'accounts/register.html' , {'form':form})
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():

            username= form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password']

            user = User(username=username , email=email , password=password1)
            user.save()
            return redirect('login')
        else:
            form = RegistrationForm()
        return render(request , 'accounts/register.html' , {'form':form})




def Userlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Your username doesn't exists!")
            
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            return redirect('profile-form')
        else:
            messages.error(request,"User does not exist.")
            return redirect('register')

    return render(request, 'accounts/login.html')


def ForgetPasswordView(request):
    form = ForgetPasswordForm()
    if request.method =="POST":
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if not User.objects.filter(email=email).first():
                messages.success(request ,"Not user Found with this email id")
                return redirect('forget-password')

            user_obj = User.objects.get(email=email)
            send_forget_password_mail(user_obj , token)
    return render(request , 'accounts/change.html',{'form':form})
