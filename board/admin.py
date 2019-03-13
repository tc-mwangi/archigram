from django.contrib import admin
from .models import Photo, Like, Follow, Member, Comment


# Crete classes for admin models
class CommentAdmin(admin.ModelAdmin):
    '''
        admin comment
    '''
    list_display = ('author', 'photo', 'text')


class PhotoAdmin(admin.ModelAdmin):
    '''
        admin view photo
    '''
    list_display = ('author', 'caption', 'published')
    

class FollowAdmin(admin.ModelAdmin):
    '''
        admin follow
    '''
    list_display = ('follower', 'following')


class LikeAdmin(admin.ModelAdmin):
    '''
        admin like
    '''
    list_display = ('author', 'published')
    

# Register your models here.
admin.site.register(Like, LikeAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Member)

