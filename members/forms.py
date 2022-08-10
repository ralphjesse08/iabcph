from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from members.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    firstName = forms.CharField(max_length=255, help_text="Required. Add a first name ")
    middleName = forms.CharField(max_length=255, help_text="Required. Add a middle name ")
    lastName = forms.CharField(max_length=255, help_text="Required. Add a lastname name ")

    class Meta: 
        model = User
        fields = ('email', 'firstName', 'middleName', 'lastName', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            member = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use. ")  
        

class BidderRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    firstName = forms.CharField(max_length=255, help_text="Required. Add a first name ")
    middleName = forms.CharField(max_length=255, help_text="Required. Add a middle name ")
    lastName = forms.CharField(max_length=255, help_text="Required. Add a lastname name ")
    is_bidder = forms.BooleanField(initial=True)

    class Meta: 
        model = User
        fields = ('email', 'firstName', 'middleName', 'lastName', 'password1', 'password2', 'is_bidder')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            member = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use. ")  

class StaffRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    firstName = forms.CharField(max_length=255, help_text="Required. Add a first name ")
    middleName = forms.CharField(max_length=255, help_text="Required. Add a middle name ")
    lastName = forms.CharField(max_length=255, help_text="Required. Add a lastname name ")
    is_staff = forms.BooleanField(initial=True)

    class Meta: 
        model = User
        fields = ('email', 'firstName', 'middleName', 'lastName', 'password1', 'password2', 'is_staff')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            member = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use. ") 