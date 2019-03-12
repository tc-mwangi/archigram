from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'board'
urlpatterns=[
    url('^$',views.timeline, name='timeline'),
    url(r'^profile/', views.user_profile, name='user_profile'),
    url(r'^upload/', views.upload_content, name='upload_content'),
    url(r'^search/', views.search_user, name='search_user'),
    url(r'^modal/', views.view_modal, name='view_modal'),
    url(r'^followers/', views.followers, name='followers'),
    url(r'^following/', views.following, name='following'),
    url(r'^post/', views.post, name='post'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




