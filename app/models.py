from distutils.command.upload import upload
from django.db import models
# from django.contrib.auth.models import User
from  accounts.models import User
# from django_countries.fields import CountryField
import os
# from django_countries.fields import CountryField

# from djangoratings.fields import RatingField
# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating

# Create your models here.



class Diary(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE ,related_name='dairy_user')
    title = models.CharField(max_length=100)
    diary_image = models.ImageField(upload_to="diary_pic",default="avatar.svg",blank=True)
    # avatar = models.ImageField(null=True, default="avatar.svg")
    make_public = models.BooleanField()

    # chapter = models.ManyToManyField(Chapter)
    # mode = models.ManyToOneRel

    def __str__(self):
        return self.title

class Chapter(models.Model):
    diary = models.ForeignKey(Diary ,on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


    def __str__(self):
        return str(self.title)

class Restaurant(models.Model):

    STATUS_rate = (
        ('★','★'),('★★','★★'),('★★★','★★★'),('★★★★','★★★★'),('★★★★★','★★★★★')
    )

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    chapter = models.ForeignKey(Chapter , on_delete=models.CASCADE)
    dish = models.CharField(max_length=100)
    rating = models.CharField(max_length=5 , choices=STATUS_rate , default='3')
    review = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    updated = models.DateTimeField(auto_now=True , blank=True)
    created = models.DateTimeField(auto_now_add=True , blank=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    COUNTRY_Choice = (
        ('India' , 'India'),('Czechia' , 'czechia'),('Asia','Asia')
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    # country = CountryField()
    country = models.CharField(max_length=15 , choices=COUNTRY_Choice)
      
    def __str__(self):
        return self.first_name
        
       
class ContactUs(models.Model):
    name = models.CharField(max_length=100)    
    email = models.EmailField(blank=False)
    your_query = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class CommentBox(models.Model):
    restaurant = models.ForeignKey(Restaurant , related_name='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
    

    

