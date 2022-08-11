from unicodedata import category
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import CreatePostForm, EditForm
from startblog.forms import CreatePostForm
from django.urls import reverse_lazy
from .models import Category, Post
from typing import Any


class HomePage(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ["-post_date"]

def category_post(request, cats):
    category_post = Post.objects.filter(category=cats)
    context = {"cats": cats, "category_post": category_post}
    return render(request, "blog/category_post.html", context)


class PostPage(DetailView):
    model = Post
    template_name = "blog/post_details.html"


class AddPost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/add_post.html"


class AddCategory(CreateView):
    model = Category
    # form_class = CreatePostForm
    template_name = "blog/add_category.html"
    fields = "__all__" 

class Createpost(View):
    def post(self, request: HttpRequest):
        if not request.user.is_authenticated:
            raise Http404("NOT LOGGED IN")

        form = CreatePostForm(request.POST)

        if form.is_valid():
            form.author = request.user
            form.save()

        new_post = Post.objects.last()
        return redirect("blog:post_details", pk=new_post.id)

    def get(self, request: HttpRequest):
        form = CreatePostForm()
        return render(request, "blog/add_post.html", {"form": form})


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/update_post.html"


class DeletePost(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:home")

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()

        if not request.user == self.object.author:
            messages.error(request, "You are not allowed to delete this object.")
            return redirect("blog:home")
        return super().post(request, *args, **kwargs)
