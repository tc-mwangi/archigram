from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/accounts/login/')
def timeline(request):
    '''displays timeline content
    
    Arguments:
        request {[type]} -- [description]
    '''


    return render(request,'main/timeline.html')

# @login_required(login_url='/accounts/login/')
def user_profile(request):
    '''displays profile page content
    
    Arguments:
        request {[type]} -- [description]
    '''

    return render(request,'user/profile.html')


def upload_content(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    '''


    return render(request,'user/upload.html')


def search_user(request):
    '''return results of user searched
    
    Arguments:
        request {[type]} -- [description]
    '''


    return render(request, 'user/search.html')


def view_modal(request):
    '''returns image modal
    
    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'user/modal.html')


def followers(request):
    '''returns image modal
    
    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'user/followers.html')


def following(request):
    '''returns image modal
    
    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'user/following.html')


def post(request):
    '''returns image modal
    
    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'user/upload.html')




