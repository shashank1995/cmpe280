from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^standings/$', views.standings, name='standings'),
	url(r'^scores/$', views.scores, name='scores')
]