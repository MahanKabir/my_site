from django.contrib.auth.models import User
from django.db import models
from category.models import Category

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='static/category/images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)