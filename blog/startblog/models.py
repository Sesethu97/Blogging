from contextlib import nullcontext
from curses.ascii import NUL
from tkinter import Widget
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class User(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to="images/profile/"
    )
    website_url = models.URLField(max_length=255, null=True, blank=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)
    pinterest_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("blog:home")


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:home")


class Post(models.Model):
    title: str = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to="photo/", null=True, blank=False)
    author: str = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING
    )
    caption: str = models.TextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislike', default=None, blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:home")


class Vote(models.Model):
    user = models.ForeignKey("startblog.User", on_delete=models.DO_NOTHING, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    has_voted = models.BooleanField(default=False)
