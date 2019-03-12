from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from board.forms import LoginForm, PhotoForm, MemberPhotoForm
from board.models import Follow, Photo, Member, Comment, Like


def index():
    '''displays index page
    '''

def user_login():
    '''displays user login form
    '''

def user_logout():
    '''displays user logout form
    '''

def upload_photo():
    '''diplays image upload form
    '''

def users():
    '''displays a list of registered users
    '''

def user_profile():
    '''displays users's profile details
    '''

def user_following():
    '''displays users that user followers
    '''

def user_followers():
    '''displays users that follow the logged in user
    '''

def feed():
    '''[summary]
    '''

def search():
    '''returns search results by user
    '''


