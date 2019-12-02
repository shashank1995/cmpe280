from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^scores/$', views.scores, name='scores'),
	url(r'^predictor/$', views.predictor, name='predictor')
]