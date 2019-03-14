from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_photo, name='upload_photo'),
    url(r'^users/$', views.users, name='users'),
    url(r'^u/(?P<username>[\w-]+)$', views.user_profile, name='user_view'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^profile/$', views.upload_user_profile_pic, name='upload_user_profile_pic'),
    url(r'^following/$', views.following, name='following'),
    url(r'^followers/$', views.follower, name='follower'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^search/$', views.search, name='user_search'),
    url(r'^see/$', views.see, name='see'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





