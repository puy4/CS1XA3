from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path

def lab7_proj(request):
     name = request.POST.get("name","")
     password = request.POST.get("password","")
     if name = "Jimmy" and if password = "Hendrix":
        html = "Cool"
     else: html = "Bad User Name"
     return HttpResponse(html)
