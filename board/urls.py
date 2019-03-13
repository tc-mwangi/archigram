from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import views
from .views import ajax


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_photo, name='upload_photo'),
    url(r'^users/$', views.users, name='users'),
    url(r'^u/(?P<username>[\w-]+)$', views.user_profile, name='user_view'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^following/$', views.following, name='following'),
    url(r'^followers/$', views.follower, name='follower'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^search/$', views.search, name='user_search'),
    url(r'^see/$', views.see, name='see'),



    # AJAX methods for uploads, follow, and comments
    url(r'^upload_dp/$', ajax.upload_user_profile_pic,
        name='upload_user_profile_pic'),
    url(r'^follow/$', ajax.follow_user, name='follow_user'),
    url(r'^unfollow/$', ajax.unfollow_user, name='unfollow_user'),
    url(r'^post_comment/$', ajax.post_photo_comment, name='post_photo_comment'),
    url(r'^like_comment/$', ajax.like_photo, name='like_photo'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





