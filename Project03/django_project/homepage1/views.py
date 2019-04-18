from django.shortcuts import render


hometitle = {'title':'A Simple Note-taking App'}


def home(request):
    return render(request, 'home.html', hometitle)
   
# Create your views here.
