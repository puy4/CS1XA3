from django.shortcuts import render
from .models import Post
from users import views as userviews
from .forms import theform, deletenotes
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


hometitle = {'title':'A Simple Note-taking App'}


def home(request):
   return render(request, 'home.html', hometitle)

def notes(request):
   notes = Post.objects.all().filter(user=request.user)
   return render(request, 'notes.html',{'notes': notes})


def uploadnotes(request):
        id = request.GET.get('id', None)
        if id is not None:
                note = get_object_or_404(Post, id=id)
        else:
                note = None

        if request.method == 'POST':
                form = theform(request.POST, instance=note)
                if form.is_valid():
                        object = form.save(commit=False)
                        object.user = request.user
                        object.save()
                        messages.add_message(request, messages.INFO, 'Note Added')
                        return HttpResponseRedirect('../notes')
        else: form = theform(instance=note)

        return render(request, 'addnotes.html', {'form':form})

def deletenotes(request):
        id = request.GET.get('id', None)
        if id is not None:
             note = get_object_or_404(Notes, id=id)
        else:
             note = None
        if request.method == 'POST':
             form = deletenotes(request.POST, instance=note)
             if form.is_valid:
                    note.delete()
                    messages.add_message(request, messages.INFO, 'Note Deleted')
                    return HttpResponseRedirect('../notes')
        else: form = deletenotes(instance=note)

        return render(request, 'notes.html', {'note':note})
