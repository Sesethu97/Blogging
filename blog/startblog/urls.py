from django.urls import path

from .views import (
    CreatePost,
    HomePage,
    PostPage,
    UpdatePost,
    DeletePost,
    category_post,
    create_post,
    category_list,
    user_cast_vote,
    base_home,
    contact_page,
)


app_name = "startblog"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("base_home", base_home, name="base_home"),
    path("contact_page", contact_page, name="contact_page"),
    path("article/<int:pk>", PostPage.as_view(), name="post_details"),
    path("add_post/", create_post, name="add_post"),
    path("article/edit/<int:pk>", UpdatePost.as_view(), name="update_post"),
    path("article/<int:pk>/delete", DeletePost.as_view(), name="delete_post"),
    path("category/<str:cats>", category_post, name="category_post"),
    path("category_list/", category_list, name="category_list"),
    path("vote/<pk>/<vote_value>", user_cast_vote, name="cast_vote"),
  
]
