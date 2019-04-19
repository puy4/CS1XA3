from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
     content = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     date = models.DateTimeField(default=timezone.now)

 
