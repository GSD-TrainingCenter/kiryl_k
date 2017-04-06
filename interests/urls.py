from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^newinterest/$', views.create_new_interest, name='newinterest'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]