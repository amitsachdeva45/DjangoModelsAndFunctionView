"""djviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import normal_request, normal_response, redirect_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^normal_request/$', normal_request, name='home'),
    url(r'^normal_response/$', normal_response, name='home'),
    url(r'^redirect/$', redirect_views, name='home'),
    url(r'^blog/', include('blog.urls')) #URLS of blog included
]
