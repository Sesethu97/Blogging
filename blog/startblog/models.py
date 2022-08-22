from contextlib import nullcontext
from curses.ascii import NUL
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
    header_image = models.ImageField(upload_to="photo/", null=True, blank=True)
    title_tag: str = models.CharField(max_length=255, default="my blog")
    author: str = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING
    )
    body: str = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    snippet = models.CharField(
        max_length=255, blank=True, null=True, default="Click Link To Read Blog Post"
    )
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
 

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:home")


class Vote(models.Model):
    user = models.ForeignKey("startblog.User", on_delete=models.DO_NOTHING, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    has_voted = models.BooleanField(default=False)
