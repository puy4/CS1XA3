from django.db import models

class Contact(models.Model):

     email = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     first_name = models.CharField(max_length=30)
     title = models.CharField(max_length=30)
     content = models.TextField()
