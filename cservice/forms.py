from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Service, Testimonial, Profile, Contact
from datetime import datetime, timedelta

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['title', 'description']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'phone', 'address', 'information', 'facebook', 'twitter', 'linkedin', 'instagram']
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'service', 'book_date', 'phone', 'email', 'message']
    
    def clean(self):
        cleaned_data = super().clean()
        book_date = cleaned_data.get('book_date')
        
        if book_date:
            datetime_obj = datetime.strptime(book_date, '%Y-%m-%dT%H:%M')
            datetime_obj = datetime_obj.replace(second=43)
            formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
            cleaned_data['book_date'] = formatted_datetime
        
        return cleaned_data

