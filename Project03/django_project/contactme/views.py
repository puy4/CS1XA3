from django.shortcuts import render
import json

def send(request):
     reqDict = json.loads(request.body.decode('utf-8'))
     firstname = reqDict.get('first_name','')
     lastname = reqDict.get('last_name','')
     email = reqDict.get('email','')
     title = reqDict.get('title','')
     content = reqDict.get('content','')
     if request.method == 'POST':
         form = thecontact(request.POST)
         if form.is_valid():
             pass
         else:
             form = thecontact()
     return render(request, 'contactme.html', {'form': form})
