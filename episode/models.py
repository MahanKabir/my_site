from django.db import models

# Create your models here.


class Episode(models.Model):
    title = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    time = models.CharField(max_length=100, null=False)
    body = models.TextField()
    video = models.FileField(upload_to='static/episode/videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)