from .models import UserProfileModel
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    """
    Form for user profile
    """
    class Meta:
        model = UserProfileModel
        fields = ['address', 'phone_number', 'birth_date']
