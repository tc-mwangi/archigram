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

    title = "timeline"
    current_user = request.user
    pic_posts = Pic.objects.all()  
    my_profile = Profile.objects.order_by('-time_uploaded')
    comments = Comment.objects.order_by('-time_comment')


    return render(request,'main/timeline.html', {"title":title,"pic_posts":pic_posts, "my_profile": my_profile, "comments":comments})




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



@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( user_profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( user_profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def send(request):
    '''
    display form for uploading images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
            image.likes +=0
            image.save() 

            return redirect( timeline)
    else:
        form = ImageForm() 
    return render(request, 'user/upload.html',{"form" : form})



@login_required(login_url='/accounts/login/')
def comment(request, id):
	
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


@login_required(login_url='/accounts/login/')
def like(request,pic_id):
    '''tally and display likes
    
    Arguments:
        request {[type]} -- [description]
        pic_id {[type]} -- [description]
    '''

    Pic = Pic.objects.get(id=pic_id)
    like +=1
    save_like()

    return redirect(timeline)



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




