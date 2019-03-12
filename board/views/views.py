from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from board.forms import LoginForm, PhotoForm, MemberPhotoForm
from board.models import Photo, Member, Follow, Comment, Like



def index(request):
    '''displays index page
    '''

    if request.user.is_authenticated():
        return HttpResponseRedirect('/insta/feed')

    return render(request, 'boardapp/index.html', {})


def feed(request):
    '''displays photo thread of following user's posts, and users posts too
    '''

    user = request.user
    photos = []
    liked_photos = []
    user_following = Follow.objects.filter(follower__id=user.id)

    for user_object in user_following:
        following_photos = Photo.objects.filter(author__id=user_object.following.id)

        if following_photos is not None:
            photos.append(following_photos)

    return render(request, 'board/feed.html', {
        'photos': photos,
        'liked_photos': liked_photos
        })



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

            return HttpResponseRedirect('/insta/upload')
    else:
        form = PhotoForm()

    return render(request, 'board/upload_photo.html', {'form': form})


def user_profile(request):
    '''displays users's profile details
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

    user_photos = Photo.objects.filter(owner__pk=user.id)
    photos_count = user_photos.count()
    return render(request, 'board/profile.html', {
        'user': user,
        'user_dp': user_dp,
        'photos': user_photos,
        'count': photos_count,
        'dp_form': upload_prof_pic_form
        })


def users(request):
    '''displays a list of registered users
    '''


    userlist = []
    users = User.objects.all()[:9]

    for user in users:
        queryset = Follow.objects.filter(
                            follower__pk=request.user.id,
                            following__pk=user.pk,
                            active=True
                            )
        follow_status = get_object_or_None(queryset)

        if follow_status is None:
            userlist.append(user)

    return render(request, 'boardapp/users.html', {'users': userlist})







def user_following(request):
    '''displays users that user followers
    '''

    user = request.user

    following = Follow.objects.filter(follower__pk=user.id, active=True)

    return render(request, 'boardapp/user_following.html', {
        'following': following
        })



def user_followers(request):
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


    return render(request, 'boardapp/user_followers.html', {
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
                                following__pk=user.pk,
                                active=True
                                )
            follow_status = get_object_or_None(queryset)

            if follow_status is not None:
                followlist.append(user.id)

    return render(request, 'boardapp/search.html', {
        'results': results,
        'followlist': followlist
        })







import json, itertools

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from board.forms import LoginForm, PhotoForm, MemberPhotoForm
from board.models import Follow, Photo, Member, Comment, Like


# Create your views here.

def follow_user(request):
    """
    Method (AJAX) that makes the `logged user` follow the selected user
    """
    data = {
            'status': 0,
        }
    if request.user.is_authenticated():
        if request.method == 'POST':
            follower = User.objects.get(pk=request.user.id)
            following = User.objects.get(pk=request.POST['uid'])

            follow = Follow(follower=follower, following=following)
            follow.save()

            # data to be returned as json
            data = {
                'status': 1,
                'follower': request.user.id,
                'to_follow': request.POST['uid']
            }

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def unfollow_user(request):
    """
    Method (AJAX) that makes the `logged user` to unfollow a selected user
    """
    data = {
        'status': 0,
    }
    if request.user.is_authenticated():
        if request.method == 'POST':
            # check if logged user is following the selected user
            follower = User.objects.get(pk=request.user.id)
            following = User.objects.get(pk=request.POST['uid'])

            follow_obj = get_object_or_None(Follow,
                                    follower=follower,
                                    following=following,
                                    active=True
                                    )

            # if is following, update `active` field to False
            if follow_obj is not None:
                follow_obj.active = False
                resp = follow_obj.save()
                # after a successful unfollow, update `data` variable's status to 1
                data['status'] = 1

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def upload_user_profile_pic(request):
    """
    Method (AJAX) that allows the `logged user` to upload a profile pic
    """
    uploader = request.user
    form = MemberPhotoForm()
    data = {
        'status': 1,
    }

    if request.method == 'POST':
        form = MemberPhotoForm(request.POST, request.FILES)
        if form.is_valid():

            # check if user has already uploaded a profile picture
            existing_dp = get_object_or_None(Member, user__pk=uploader.id)

            obj = form.save(commit=False)
            obj.user = uploader

            if existing_dp is not None:
                obj.id = existing_dp.id

            obj.save()

            data['status'] = 1

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')



def post_photo_comment(request):
    data = {
        'status': 0
    }

    if request.user.is_authenticated() and request.method == 'POST':
        post_data = request.POST

        photo = get_object_or_None(Photo, pk=post_data['photo_id'])
        comment = Comment(
            owner=request.user.member,
            photo=photo,
            text=post_data['comment_text']
            )
        resp = comment.save()
        data['status'] = 1

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def like_photo(request):
    data = {
        'status': 0
    }

    # TODO: Check if like already exists
    if request.user.is_authenticated() and request.method == 'POST':
        post_data = request.POST

        photo = get_object_or_None(Photo, pk=post_data['photo_id'])

        check_like = get_object_or_None(Like,
            owner=request.user.member,
            photo=photo
            )

        if check_like is None:
            like = Like(
                owner=request.user.member,
                photo=photo,
                )
            like.save()
            data['status'] = 1

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')



