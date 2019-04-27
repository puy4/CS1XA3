from django.shortcuts import render
from django import forms
from .forms import thecontact
import json

def send(request):

     if request.method == 'POST':
         form = thecontact(request.POST)
         if form.is_valid():
             pass
         else:
             form = thecontact()
     return render(request, 'contactme.html', {'form': form})
