from django.shortcuts import render
from .models import Post
from users import views as userviews

hometitle = {'title':'A Simple Note-taking App'}


def home(request):
    return render(request, 'home.html', hometitle)

def notes(request):
   notes = Post.objects.all().filter(user=request.user)
   return render(request, 'notes.html',{'notes': notes})

##def uploadnotes(request):
   


