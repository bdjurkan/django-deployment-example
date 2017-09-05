"""
DocString for 'basic_app/models.py'
"""
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    """ class DocString """

    user = models.OneToOneField(User)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic    = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        """ return class as a string """
        return self.user.username
