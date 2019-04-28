from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

<!--
registration.
-->

def register(request):
    if request.method =='POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
              form.save()
              messages.success(request, 'Account Created, you can now log in!')
              return redirect('login')
    else:
         form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
