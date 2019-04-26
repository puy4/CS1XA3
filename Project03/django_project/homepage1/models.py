from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispath import receiver

class Post(models.Model):
     content = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     date = models.DateTimeField(default=timezone.now)
