"""
DocString for 'basic_app/forms.py'
"""
from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    """ class DocString """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        """ class DocString """
        model  = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    """ class DocString """

    class Meta():
        """ class DocString """
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
