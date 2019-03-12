from django.db import models
from django.contrib.auth.models import User



class Photo(models.Model):
	'''creates instances of photos 
	'''

	author = models.ForeignKey(User, related_name='+', null=True)
	caption = models.TextField(max_length=255)
	image = models.ImageField(upload_to="uploads/photos", null=True)
	published = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.caption


class Member(models.Model):
	'''creates instances of registered members
	'''

	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="uploads/dp", null=True)
	modified = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.user


class Like(models.Model):
	'''creates instances of likes 
	'''
	
	author = models.ForeignKey(Member, null=True)
	photo = models.ForeignKey(Photo, null=True)
	published = models.DateTimeField(auto_now_add=True)
	

class Follow(models.Model):
	'''creates instances of folowers and following
	'''

	follower = models.ForeignKey(User, related_name='+', null=True)
	following = models.ForeignKey(User,related_name='+', null=True)
	

	def get_follower(self):
		return self.follower


	def get_following(self):
		return self.following


class Comment(models.Model):
	'''creates instances on comments
	'''
	author = models.ForeignKey(Member, null=True)
	photo = models.ForeignKey(Photo, null=True)
	text = models.TextField(max_length=140)
	published = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.text


