from django import forms
from .models import Image, Comment ,Profile
from django.contrib.auth.forms import AuthenticationForm



class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Image
		image_pic = forms.ImageField(label = 'Image Field')


class ProfileUploadForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	bio = forms.CharField(label='Image Caption',max_length=300)
	profile_pic = forms.ImageField(label = 'Image Field')


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment	
		exclude = ['user','pic',]





