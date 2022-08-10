from django.urls import path

# from . import views
from .views import Createpost, HomePage, PostPage, UpdatePost, DeletePost, AddCategory, Category


app_name = "startblog"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("article/<int:pk>", PostPage.as_view(), name="post_details"),
    path("add_post/", Createpost.as_view(), name="add_post"),
    path("article/edit/<int:pk>", UpdatePost.as_view(), name="update_post"),
    path("article/<int:pk>/delete", DeletePost.as_view(), name="delete_post"),
    path("add_category", AddCategory.as_view(), name="add_category"),
    path("category/<str:cats>/", Category, name="add_category"),

]
