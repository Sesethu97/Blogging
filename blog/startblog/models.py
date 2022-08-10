from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse("blog:home")

choices =[("uncategorized", "uncategorized"),("sports", "sports"),("food&drinks", "food&drinks"),("entertainment", "entertainment"),("fashion", "fashion"),("photography&arts", "photography&arts"),("travels", "travels")]

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="my blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.title + " | " + str(self.author)


    def get_absolute_url(self):
        return reverse("blog:home")