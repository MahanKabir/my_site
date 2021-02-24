from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    describe = models.TextField()
    price = models.DecimalField(max_digits= 15, decimal_places=3, null=False)
    image = models.ImageField(upload_to='static/course/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
