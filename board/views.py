from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

def homepage(request):
    '''displays homepage content
    
    Arguments:
        request {[type]} -- [description]
    '''


    return render(request,'main/landing.html')


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




