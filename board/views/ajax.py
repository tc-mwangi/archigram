import json, itertools

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from board.forms import LoginForm, PhotoForm, MemberPhotoForm
from board.models import Follow, Photo, Member, Comment, Like

from annoying.functions import get_object_or_None

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
