"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # Add include to the imports here
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from sportnews.views import test_results
from accounts.views import main_view, AboutPageView, ContactPageView, ServicesPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('accounts.urls')),
    url(r'^', include('sportnews.urls')), # tell django to read urls.py in example app
    url(r'^', include('sportscores.urls')),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('redirect/', main_view),
    url(r'^about/$', AboutPageView.as_view(), name='about'),
    url(r'^contact/$', ContactPageView.as_view(), name='contact'),
    url(r'^services/$', ServicesPageView.as_view(), name='services'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
