from django.urls import path

# from . import views
from .views import Createpso, HomePage, PostPage, UpdatePost, DeletePost


app_name = "startblog"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("article/<int:pk>", PostPage.as_view(), name="post_details"),
    path("add_post/", Createpso.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/<int:pk>/delete',	DeletePost.as_view(), name="delete_post"),
]
