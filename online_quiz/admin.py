from django.contrib import admin
from .models import Test, Profile, Feedbackk, reporting, ResultsPredictions
from django.urls import path

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

class reportingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'location', 'gender', 'attempt_correct', 'time')
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
admin.site.register(reporting, reportingAdmin)
admin.site.register(ResultsPredictions)
admin.site.site_header = 'BestFit Organization'
admin.site.index_title = 'BestFit Administration'
admin.site.site_title = 'Admin pannel of bestfit organization'


