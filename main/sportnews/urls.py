# 

from django.conf.urls import url, include
from sportnews import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^login/$', views.LoginPageView.as_view(), name='login'),
    path('', include('social_django.urls', namespace='social')),
    url(r'^sportnews/$', views.sportnews, name='sportnews'),
    url(r'^testnews/$', views.test_results, name='testnews'),
]