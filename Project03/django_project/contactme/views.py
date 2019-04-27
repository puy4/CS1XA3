from django.shortcuts import render

def send(request):
     body_unicode = request.body.decode('utf-8')
     reqDict = json.loads(body_unicode)
     firstname = reqDict.get('first_name','')
     lastname = reqDict.get('last_name','')
     email = reqDict.get('email,'')
     title = reqDict.get('title,'')
     content = reqDict.get('content','')
