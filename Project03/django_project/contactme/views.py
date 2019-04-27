from django.shortcuts import render
from django import forms
from .forms import thecontact
import json

def validateemail(request):
    email = request.POST.get('email',none)
    data = { include@ : Contact.objects.filter(email__contains='@')}
    return JsonResponse(data)


def send(request):

    if request.method == 'POST':
        form = thecontact(request.POST)
        if form.is_valid():
            form = form.cleaned_data

    else:
        form = thecontact()
    return render(request, 'contactme.html', {'form': form})
