"""control URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from control.users.views import (
    signup,
    view_profile,
    edit_profile,
    password_reset,
    account_deletion,
    delete_confirmation
)
from control.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/$', view_profile, name='view_profile'),
    url(r'^profile/edit_profile/$', edit_profile, name='edit_profile'),
    url(r'^profile/password_reset/$', password_reset, name='password_reset'),
    url(r'^profile/delete_confirmation/$', delete_confirmation, name='delete_confirmation'),
    url(r'^profile/delete/(?P<user_id>\d+)/$', account_deletion, name='account_deletion'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
