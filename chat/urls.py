from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chat/$', views.chat, name='post'),
    
    url(r'^post/$', views.post, name='post'),
	url(r'^messages/$', views.messages, name='messages'),
]