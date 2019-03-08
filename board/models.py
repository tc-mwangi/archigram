from django.db import models
import datetime as datetime
from django import forms
from django.contrib.auth.models import User
#from fontawesome.fields import IconField
# from tinymce.models import HTMLField







class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    '''

    profile_pic = models.ImageField(upload_to='profiles/', null=True)
    # bio = HTMLField()
    #icon = IconField()
    #from fontawesome


class tags(models.Model):
    '''creates instances of image tags
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    '''creates instances of images uploaded to profile

    Arguments:
    models {[type]} -- [description]
    '''

    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=60)
    profile = models.ForeignKey(Profile)
    post_image = models.ImageField(upload_to = 'images/', null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)
   






