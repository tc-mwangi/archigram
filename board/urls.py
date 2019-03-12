from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import views

app_name = 'board'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^login/$', views.user_login, name='user_login'),
    # url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^upload/$', views.upload_photo, name='upload_photo'),
    url(r'^users/$', views.users, name='users'),
    url(r'^u/(?P<username>[\w-]+)$', views.user_profile, name='user_view'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^following/$', views.user_following, name='user_following'),
    url(r'^followers/$', views.user_followers, name='user_followers'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^search/$', views.search, name='user_search'),

    # AJAX methods
    url(r'^upload_dp/$', views.upload_user_profile_pic,
        name='upload_user_profile_pic'),
    url(r'^follow/$', views.follow_user, name='follow_user'),
    url(r'^unfollow/$', views.unfollow_user, name='unfollow_user'),
    url(r'^post_comment/$', views.post_photo_comment, name='post_photo_comment'),
    url(r'^like_comment/$', views.like_photo, name='like_photo'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





