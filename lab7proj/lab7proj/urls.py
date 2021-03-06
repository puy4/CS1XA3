"""lab7proj URL Configuration

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
from django.urls import path
from django.http import HttpResponse

def lab7_proj(request):
     name = request.POST.get("name","")
     password = request.POST.get("password","")
     if name == "Jimmy" and password == "Hendrix":
        html = "Cool"
     else: html = "Bad User Name"
     return HttpResponse(html)



urlpatterns = [
    path('e/puy4/',lab7_proj, ),
]
