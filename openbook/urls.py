"""openbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin

from openbook_auth.views import Register, UsernameCheck, EmailCheck

auth_patterns = [
    path('register/', Register.as_view(), name='register-user'),
    path('username-check/', UsernameCheck.as_view(), name='username-check'),
    path('email-check/', EmailCheck.as_view(), name='email-check'),
]

api_patterns = [
    path('auth/', include(auth_patterns)),
]

urlpatterns = [
    path('api/', include(api_patterns)),
    url('admin/', admin.site.urls),
]