from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm

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


def resetpassword(request):
    if request.method =='POST':
        form = SetPasswordForm(reques.POST)
        if form.is_valid():
            form.save()
            messsages.success(request, 'password reset successful')
            return redirect('login')
    else:
        form = SetPasswordForm()
    return render(request, 'passwordreset.html',{'form': form})
