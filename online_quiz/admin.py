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
        'gender'
        )
    search_fields = (
        '^first_name', 
        '^last_name', 
        )
    list_filter = (
        'first_name', 
        'last_name', 
        'location', 
        'gender'
        )


# class questionAdmin(admin.ModelAdmin):
#     list_filter = ('qustion', 'answer')

admin.site.register(Test, TestAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Feedbackk)
admin.site.register(ResultsPredictions)
# # admin.site.site_header = 'BestFit Organization'
# admin.site.index_title = 'BestFit Administration'
# admin.site.site_title = 'Admin pannel of bestfit organization'
# admin.site.index_template = 'admin/index_template.html'


