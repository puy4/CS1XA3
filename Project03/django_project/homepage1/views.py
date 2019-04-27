from .models import Post
from users import views as userviews
from .forms import theform
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import json
import request



hometitle = {'title':'A Simple Note-taking App'}


def home(request):
   return render(request, 'home.html', hometitle)


def contactmeagain(request):
    reqDict = json.loads(request.body).decode('utf-8')
    subject = reqDict.get('reason','')
    from_email = reqDict.get('Email1', '')
    message = reqDict.get('text', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email,['lancepp@protonmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('contactmeagain/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')


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
