from django.urls import path

from .views import (
    CreatePost,
    DislikeView,
    HomePage,
    PostPage,
    UpdatePost,
    DeletePost,
    category_post,
    create_post,
    category_list,
    base_home,
    LikeView
    
)


app_name = "startblog"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("base_home", base_home, name="base_home"),
    path("article/<int:pk>", PostPage.as_view(), name="post_details"),
    path("add_post/", create_post, name="add_post"),
    path("article/edit/<int:pk>", UpdatePost.as_view(), name="update_post"),
    path("article/<int:pk>/delete", DeletePost.as_view(), name="delete_post"),
    path("category/<str:cats>", category_post, name="category_post"),
    path("category_list/", category_list, name="category_list"),
    path("likes/<int:pk>", LikeView, name="likes"),
    path("dislikes/<int:pk>", DislikeView, name="dislikes"),

  
]
