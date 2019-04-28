from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import json

def register(request):
    jreq = json.loads(request.body)
    username = jreq.get('username','')
    password = jreq.get('password','')
    reenterpas = jreq.get('reenterpas','')
    if password == reenterpas and len(password) > 8 and  username !="":
              user = User.objects.create_user(username=username, password=password)
              user.asve()
              messages.success(request, 'Account Created, you can now log in!')
              return redirect('login')
    else:
         return HttpResponse('login fails')
   
