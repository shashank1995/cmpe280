# 

from django.conf.urls import url, include
from sportnews import views
from django.urls import path

urlpatterns = [
    #url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    path('', include('social_django.urls', namespace='social')),
    url(r'^sportnews/$', views.sportnews, name='sportnews'),
]