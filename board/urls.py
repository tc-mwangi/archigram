from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.timeline, name='timeline'),
    url(r'^profile/', views.user_profile, name='user_profile'),
    url(r'^upload/', views.upload_content, name='upload_content'),
    url(r'^search/', views.search_user, name='search_user'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)