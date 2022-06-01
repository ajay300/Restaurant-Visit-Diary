# from itertools import product
# from xml.etree.ElementTree import Comment
# from http.client import HTTPResponse
from genericpath import exists
from django.shortcuts import render , redirect ,HttpResponse
from django.views import View
from .forms import CommentForm, DiaryForm, ProfileForm, chapterform , RestaurantForm , ContactForm
from django.contrib.auth import login
from .models import ContactUs, Diary , Chapter, Profile ,Restaurant ,CommentBox
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import User


# Create your views here.
# Home
def home(request):
    diary = Diary.objects.filter(make_public = 1)
    profile = Profile.objects.all()
    context = { 'diary':diary , 'profile':profile}

    return render(request , 'app/home.html' , context)


class ChapterView(View):
    def get(self , request ,pk):
        chapter = Chapter.objects.filter(diary = pk)
        resto = Restaurant.objects.filter(chapter_id=pk)
        restaurant = Restaurant.objects.all()
        chapterview = Chapter.objects.all()
    
        context = {'chapter':chapter , 'resto':resto,'restaurant':restaurant,'chapterview':chapterview}
        return render(request , 'app/diary_chapter_view.html' , context)    
    
# Profile VIew
class ProfileFormView(View):

    def get(self , request):
        pk = request.user.id
        if  Profile.objects.filter(user_id=pk):                  # If request.user is New user so it will have to fill up profile details first
            return redirect('home')
        else:
            form = ProfileForm()   
        context = {'form':form}
        return render(request , 'app/profile_form.html' , context)
    
    def post(self , request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            country = form.cleaned_data['country']

            data = Profile(user=user , first_name=fname , last_name=lname , country=country)
            data.save()
            return redirect('home')

        context = {'form':form}
        return render(request , 'app/profile_form.html' , context)

def ProfileView(request , pk):

    profile = Profile.objects.get(id=pk)
    chapter = Chapter.objects.get(id=pk)
    diary = Diary.objects.get(id=pk)
    restaurant = Restaurant.objects.get(id=pk)
    context = {'profile':profile , 'diary':diary , 'chapter':chapter , 'restaurant':restaurant}
    return render(request , 'app/profile_user.html' , context)


# REstaurant View
class RestaurantView(View):
    def get(self , request , pk):
        resto = Restaurant.objects.get(pk=pk)
        
        chap = Chapter.objects.get(id=pk)
        comments = CommentBox.objects.filter(restaurant_id = pk)
        # room.participants.add(request.user)
        # profile = Profile.objects.get(id=pk)

        context = {'resto':resto , 'comments':comments ,'chap':chap }
        return render(request , 'app/restaurant_view.html' , context)    
    
    def post(self , request , pk):

        resto = Restaurant.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.user.username
            restaurant = resto
            body = form.cleaned_data['body']

            data = CommentBox(name=name , body=body,restaurant=restaurant)
            data.save()
            return redirect('resto-detail' , pk=resto.id)
        return render(request , 'app/restaurant_view.html')


@login_required(login_url='login')
def restaurantForm(request , pk ):

    form = RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            location = form.cleaned_data['Location']
            chapter_id = pk
            dish = form.cleaned_data['dish']
            rating = form.cleaned_data['rating']
            review = form.cleaned_data['review']

            data = Restaurant(user=user,name=name,Location=location,chapter_id=chapter_id,dish=dish,rating=rating,review=review)
            data.save()
            

    return render(request,'app/restaurant_form.html' , {'form':form})


class AddChapter(View):
    def get(self , request):
        chapter = Chapter.objects.all()
        form = chapterform()
        context = {'form':form , 'chapter':chapter}
        return render(request , 'app/chapter_form.html' , context)

    def post(self , request):
        form = chapterform(request.POST)
        if form.is_valid():
            user_id = request.user
            title = form.cleaned_data['title']
            diary_id = form.cleaned_data['diary']
            
            data = Chapter(user=user_id , title=title , diary=diary_id)
            data.save()
            return redirect('home')
        return render(request , 'app/chapter_form.html' , {'chap':form })

@login_required(login_url='login')
def deleteChapter(request , pk):
    chapter = Chapter.objects.get(id=pk)
    if request.method == "POST":
        chapter.delete()
        return redirect('dashboard')
    context = {'chapter':chapter}
    return render(request , 'app/chapter_delete.html' , context)




# Add diary = CRUD
class AddDiary(View):
    def get(self ,request):
        form = DiaryForm()
        return render(request , 'app/diary_form.html' , {'form':form})

    def post(self , request):
        form = DiaryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('dashboard')
        return render(request , 'app/diary_form.html' , {'form':form})

def UpdateDiary(request , pk):

    diary = Diary.objects.get(id=pk)
    form = DiaryForm(instance=diary)

    if request.user.id != diary.user.id:
        return HTTPResponse("you are not allowed Here.!")

    if request.method == "POST":
        form = DiaryForm(request.POST)
        form.is_valid()
        form.save()
        return redirect('home')

    return render(request , 'app/diary_form.html')

def DeleteDiary(request , pk):

    diary = Diary.objects.get(id=pk)

    if request.method == "POST":
        diary.delete()
        return redirect('home')

    context = {'diary':diary}
    return render(request , 'app/delete_diary.html' , context)


# Contact us Form 

class ContactFormView(View):

    def get(self , request):
        form = ContactForm()
        return render(request , 'app/contact_form.html' , {'form':form})
    
    def post(self , request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            query = form.cleaned_data['your_query']

            data = ContactUs(name=name , email=email , your_query=query)
            data.save()
            return redirect('home')
        return render(request , 'app/contact_form.html' , {'form':form})

@login_required(login_url='login')
def Dashboard(request):

    pk = request.user 
    
    diary = Diary.objects.filter(user_id=pk)
    context = {'diary':diary}
    return render(request , 'app/diary_dashboard.html' , context )


def profielUser(request , pk):
    profile = Profile.objects.get(user_id=pk)
    chapter = Chapter.objects.get(id=pk)
    diary = Diary.objects.get(id=pk)
    restaurant = profile
    profile = Profile.objects.filter(country="India")

    return render(request , 'app/profile.html' , {'profile':profile})

