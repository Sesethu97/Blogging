from distutils.command import upload
from email.mime import image
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:home")


choices = [
    ("uncategorized", "uncategorized"),
    ("sports", "sports"),
    ("food&drinks", "food&drinks"),
    ("entertainment", "entertainment"),
    ("fashion", "fashion"),
    ("photography&arts", "photography&arts"),
    ("travels", "travels"),
]


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="*image/")
    title_tag = models.CharField(max_length=255, default="my blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
   

    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    snippet = models.CharField(max_length=255, default="Click Link To Read Blog Post")
    likes = models.ManyToManyField(User, related_name="like_post")
    dislikes = models.ManyToManyField(User, related_name="dislike_post")


    def total_dislikes(self):
        return self.dislikes.count()
    


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:home")

