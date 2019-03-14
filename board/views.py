from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from board.forms import LoginForm, PhotoForm, MemberPhotoForm
from board.models import Photo, Member, Follow, Comment, Like

from annoying.functions import get_object_or_None

import json, itertools


def index(request):
    '''displays landing page with not logged in user navigation options
    '''

    if request.user.is_authenticated():
        return HttpResponseRedirect('/insta/profile')
    

    return render(request, 'boardapp/index.html', {})


@login_required(login_url='/accounts/login')
def feed(request):
    '''displays user's posts and following users's posts
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    user = request.user
    photos = []
    liked_photos = []
    user_following = Follow.objects.filter(follower__id=user.id)
    print(user_following)

    for user_object in user_following:
        following_photos = Photo.objects.filter(author__id=user_object.following.id)

        if following_photos is not None:
            photos.append(following_photos)


    for photo in photos:
        photo_like = get_object_or_None(Like,
           
            photo=photo
            )
        if photo_like:
            liked_photos.append(photo.pk)

    return render(request, 'boardapp/feed.html', {
        'photos': photos,
        'liked_photos': liked_photos
        })


@login_required(login_url='/accounts/login')
def users(request, ):
    '''displays a list of registered users
    '''
    userlist = []
    users = User.objects.all()
    print(users)

    for user in users:
        queryset = Follow.objects.filter(
                            follower__pk=request.user.id,
                            following__pk=user.pk,
                            
                            )
        follow_status = get_object_or_None(queryset)
        print(follow_status)

        if follow_status is None:
            userlist.append(user)

    return render(request, 'boardapp/users.html', {'users': userlist})



@login_required(login_url='/accounts/login')
def upload_photo(request):
    '''diplays image upload form, allows user to upload photo
    '''

    user_posting = request.user
    form = PhotoForm()

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = user_posting
            obj.save()

            return HttpResponseRedirect('/insta/profile')
    else:
        form = PhotoForm()

    return render(request, 'boardapp/upload_photo.html', {'form': form})


@login_required(login_url='/accounts/login')
def user_profile(request, username=None):
    '''display the `logged user's` profile and uploaded photos
    
    Arguments:
        request {[type]} -- [description]
    
    Keyword Arguments:
        username {[type]} -- [description] (default: {None})
    
    Returns:
        [type] -- [description]
    '''
    upload_prof_pic_form = MemberPhotoForm()

    if username is None:
        user = request.user

    else:
        user = User.objects.get(username=username)

    dp_obj = get_object_or_None(Member, user__pk=user.id)
    if dp_obj is None:
        user_dp = False
    else:
        user_dp = dp_obj

    user_photos = Photo.objects.filter(author__pk = user.id)
    photos_count = user_photos.count()
    print(photos_count)
    return render(request, 'boardapp/profile.html', {
        'user': user,
        'user_dp': user_dp,
        'photos': user_photos,
        'count': photos_count,
        'dp_form': upload_prof_pic_form
        })


def upload_user_profile_pic(request):
    """
    ajax method for profile photo image upload
    """
    user_uploading = request.user
    form = MemberPhotoForm()
    data = {
        'status': 1,
    }

    if request.method == 'POST':
        form = MemberPhotoForm(request.POST, request.FILES)
        if form.is_valid():

            # check if user has already uploaded a profile picture
            existing_dp = get_object_or_None(Member, user__pk=user_uploading.id)

            obj = form.save(commit=False)
            obj.user = user_uploading

            if existing_dp is not None:
                obj.id = existing_dp.id

            obj.save()

            data['status'] = 1

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/accounts/login')
def following(request):
    '''displays users that user followers
    '''

    user = request.user

    following = Follow.objects.filter(follower__pk=user.id)

    return render(request, 'boardapp/following.html', {
        'following': following
        })


@login_required(login_url='/accounts/login')
def follower(request):
    '''displays users that follow the logged in user
    '''

    followers = Follow.objects.filter(following__pk=request.user.id)

    # Check if you follow the users who follow you
    for user in followers:
        queryset = Follow.objects.filter(
            follower__id=request.user.id,
            following__id=user.follower.id
            )
        user.is_followed = get_object_or_None(queryset)


    return render(request, 'boardapp/followers.html', {
        'followers': followers,
        })


def search(request):
    '''returns search results by user
    '''

    query = request.GET.get('q', '')

    followlist = []
    results = User.objects.filter(username__contains=query)

    # Check follow status on a result
    if request.user.is_authenticated():
        for user in results:
            queryset = Follow.objects.filter(
                                follower__pk=request.user.id,
                                following__pk=user.pk
                                )
            follow_status = get_object_or_None(queryset)

            if follow_status is not None:
                followlist.append(user.id)

    return render(request, 'boardapp/search.html', {
        'results': results,
        'followlist': followlist
        })



def see(request,username=None):
    '''displays html views for testing visual aspects of the app
    '''
    if username is None:
        user = request.user

    else:
        user = User.objects.get(username=username)

    dp_obj = get_object_or_None(Member, user__pk=user.id)
    if dp_obj is None:
        user_dp = False
    else:
        user_dp = dp_obj

    user_photos = Photo.objects.filter(author__pk = user.id)

    

    return render(request, 'boardapp/see.html', {
        'user': user,
        'user_dp': user_dp,
        'photos': user_photos,
        })




   


