"""django_project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from users import views as userviews
from django.contrib.auth import views as authviews
from contactme import views as contviews


urlpatterns = [
    path('e/puy4/admin/', admin.site.urls),
    path('e/puy4/', include('homepage1.urls')),
    path('e/puy4/register/', userviews.register, name='register'),
    path('e/puy4/login/', authviews.LoginView.as_view(template_name='login.html'), name='login'),
    path('e/puy4/logout/', authviews.LogoutView.as_view(template_name='logout.html'), name='logout'),
    ]
