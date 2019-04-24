from django.shortcuts import render
from .models import Post
from users import views as userviews

hometitle = {'title':'A Simple Note-taking App'}


def home(request):
    return render(request, 'home.html', hometitle)

def notes(request):
    context = {'notes':Post.objects.all()}
    return render(request, 'notes.html', context)

def notesinput(request):
    if request.method == 'POST':
        input = 
