from django.shortcuts import render
from django import forms
from .forms import thecontact
import json

from django.contrib import messages



def send(request):

    if request.method == 'POST':
        form = thecontact(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            messages.success(request,a[0])


    else:
        form = thecontact()
    return render(request, 'contactme.html', {'form': form})
