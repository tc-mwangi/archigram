from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url(r'^profile/', views.user_profile, name='profile'),
    url(r'^/', views.upload_content, name='upload')
    
    ]