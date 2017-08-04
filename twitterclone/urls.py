"""twitterclone URL Configuration

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
from twitterclone_app import views

app_name = 'twitterclone'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^tweets$', views.public, name='public'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<username>\w{0,30})/$', views.users),
    url(r'^follow$', views.follow, name='follow'),
]


"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'twitterclone_app.views.index'),
    url(r'^login$', 'twitterclone_app.views.login_view'),
    url(r'^logout$', 'twitterclone_app.views.logout_view'),
    url(r'^signup$', 'twitterclone_app.views.signup'),
]
"""