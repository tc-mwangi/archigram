from django.shortcuts import render,redirect,get_object_or_404
from . forms import ProfileUploadForm ,CommentForm ,ProfileForm
from django.http  import HttpResponse
from . models import Pic ,Profile, Likes, Follow, Comment
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def timeline(request):
    '''displays timeline content
    
    Arguments:
        request {[type]} -- [description]
    '''
    pic_posts = Pic.objects.all()
    title = "archigram"


    return render(request,'main/timeline.html', {"title":title,"pic_posts":pic_posts})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    '''displays profile page content
    
    Arguments:
        request {[type]} -- [description]
    '''
    current_user = request.user
    profile = Profile.objects.all()
    follower = Follow.objects.filter(user = profile)

    return render(request, 'user/profile.html',{"current_user":current_user,"profile":profile,"follower":follower})



def upload_content(request):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
    '''


    return render(request,'user/upload.html')


@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	post = get_object_or_404(Pic,id=id)	
	current_user = request.user

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.pic = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'comment.html', {"form":form}) 





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




