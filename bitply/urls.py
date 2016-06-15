"""bitply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # index url, to create new short url
    url(r'^$', views.Index.as_view(), name='index'),
    # Url info, to get information about a short url
    url(r'^!(?P<short_url>[a-zA-Z0-9]+)$', views.UrlInfo.as_view(), name='url_info'),
    # Redirec to url, to get redirected to an url
    url(r'^(?P<short_url>[a-zA-Z0-9]+)$', views.RedirectToUrl.as_view(), name='redirect_to_url'),
]
