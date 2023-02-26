"""server_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from .auth_api import urlpatterns as authUrlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_auth/", include(authUrlpatterns)),
    path("api_air_one/", include("api_air_one.urls")),
    path("api_menu_app/", include("api_menu_app.urls")),
    path("api_online_store/", include("api_online_store.urls")),
]
