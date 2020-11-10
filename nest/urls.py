"""nest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from app.views import snoop, api_key, token_auth, basic_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snoop/', snoop, name='snoop'),
    path('api_key/', api_key, name='api_key'),
    path('token_auth/', token_auth, name='token_auth'),
    path('basic_auth/', basic_auth, name='basic_auth'),

]
