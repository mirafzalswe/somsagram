from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Postlar(models.Model):
    image = models.FileField(upload_to='media/')
    title = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts-home')

