# accounts/urls.py
from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import TemplateView # new
from . import views


urlpatterns = [
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    #path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.add_profile, name='profile'),
    path('update/', views.update_profile, name='update'),
    #path('main/', views.main_view, name='main'),
    #path('profile/main/', views.main_view, name='main'),
]

