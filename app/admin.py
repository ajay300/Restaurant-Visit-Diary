from django.contrib import admin
from .models import CommentBox, Diary , Chapter ,Restaurant , Profile

# # admin.site.register()

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','country']



@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','diary']



@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['user','title','diary_image']

@admin.register(Restaurant)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ['user','name','Location','chapter','rating']

@admin.register(CommentBox)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['restaurant','name','body','date_added']


