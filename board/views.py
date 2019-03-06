from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect


def timeline(request):
    '''displays timeline content
    
    Arguments:
        request {[type]} -- [description]
    '''


    return render(request,'main/timeline.html')


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





