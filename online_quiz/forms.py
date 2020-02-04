from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from bestfit import settings
from .models import Profile, Feedbackk
from django.forms.widgets import DateInput


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [ 'birth_date','bio', 'location','gender', 'image']
        labels = {
            'birth_date': ('Dath of Birth'),
        }
        widgets = {
        'birth_date': DateInput(attrs={'type': 'date'})
    }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbackk
        fields = ['name','email','phone','Feedback']


        