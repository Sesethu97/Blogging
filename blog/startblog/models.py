from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class User(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to="image/profile/"
    )
    website_url = models.URLField(max_length=255, null=True, blank=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)
    pinterest_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:home")


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


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="user")
#     bio = models.TextField()
#     profile_picture = models.ImageField(null=True, blank=True, upload_to="image/profile/")
#     # website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     pinterest_url = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return str(self.user)


class Post(models.Model):
    title: str = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="image/")
    title_tag: str = models.CharField(max_length=255, default="my blog")
    author: str = models.ForeignKey(User, on_delete=models.CASCADE)
    body: str = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    snippet = models.CharField(max_length=255, default="Click Link To Read Blog Post")
    # likes = models.IntegerField(default=0, blank=True)
    # has_voted = models .BooleanField(default=False)
    # likes = models.ManyToManyField(User, null=True, blank=False, related_name="like_post")
    # dislikes = models.ManyToManyField(User, null=True, blank=False,  related_name="dislike_post")

    # def total_dislikes(self):
    #     return self.dislikes.count()

    # def total_likes(self):
    #     return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:home")
