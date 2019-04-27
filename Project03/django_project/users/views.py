from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib import messages


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
        formm = SetPasswordForm(reques.POST)
        if formm.is_valid():
            formm.save()
            messsages.success(request, 'password reset successful')
            return redirect('login')
    else:
        formm = SetPasswordForm()
    return render(request, 'passwordreset.html',{'formm': formm})
