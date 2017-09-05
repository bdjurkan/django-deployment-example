"""
DocString for 'basic_app/views.py'

https://www.python.org/dev/peps/pep-0008/#imports
Imports should be grouped in the following order:

 - standard library imports
 - related third party imports
 - local application/library specific imports

You should put a blank line between each group of imports.

Example of violation:

from my_package import my_module
from django.db import models
import os

Correct way to import:

import os

from django.db import models

from my_package import my_module
"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from basic_app.forms import UserForm, UserProfileInfoForm
# Create your views here.


def index(request):
    """ method DocString """
    return render(request, 'basic_app/index.html')


@login_required
def special(request):
    """ method DocString """
    return HttpResponse('You are logged in, nice!')


@login_required
def user_logout(request):
    """ method DocString """
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """ method DocString """

    registered = False

    if request.method == 'POST':
        user_form    = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):
    """ method DocString """

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password: {}'.format(username, password))
            return HttpResponse('Invalid login details supplied!')

    return render(request, 'basic_app/login.html', {})
