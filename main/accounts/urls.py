# accounts/urls.py
from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import TemplateView # new
from . import views


urlpatterns = [
	url(r'^$', views.signup, name='account_home'),
	#path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    path('profile/', views.add_profile, name='profile'),
    path('update/', views.update_profile, name='update'),
]

