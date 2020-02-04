from django.contrib import admin
from .models import Test, Profile, Feedbackk, ResultsPredictions
# from django.contrib.auth.models import Group
from django.urls import path
#from django.utils.html import format_html 

class TestAdmin(admin.ModelAdmin):
    list_display = (
        'question', 
        "option_1", 
        "option_2", 
        'option_3', 
        'option_4', 
        "answer"
        )
    search_fields = (
        'question', 
        "option_1", 
        "option_2", 
        'option_3', 
        'option_4', 
        "answer"
        )
    list_filter = (
        'question', 
        "option_1", 
        "option_2", 
        'option_3', 
        'option_4', 
        "answer"
        )


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'location', 
        'gender',
        'birth_date',
        'image',
        )
    search_fields = (
        '^first_name', 
        '^last_name',
        'location',
        )
    list_filter = (
        'first_name', 
        'last_name', 
        'location', 
        'gender'
        )


admin.site.register(Test, TestAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Feedbackk)
admin.site.register(ResultsPredictions)
