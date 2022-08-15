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
from django.urls import reverse_lazy, reverse
from .models import Category, Post
from typing import Any
from django.http import HttpResponseRedirect


# def dislike_view(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get("post_id"))
#     disliked = False
#     if post.dislikes.filter(id=request.user.id).exists():
#         post.dislikes.remove(request.user)
#         disliked = False
#     else:
#         post.dislikes.add(request.user)
#         disliked = True

#     return HttpResponseRedirect(reverse("blog:post_details", args=[str(pk)]))


# def like_view(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get("post_id"))
#     liked = False

#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True

#     return HttpResponseRedirect(reverse("blog:post_details", args=[str(pk)]))


class HomePage(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def category_list(request):
    category_menu_list = Category.objects.all()

    context = {"category_menu_list": category_menu_list}
    return render(request, "blog/category_list.html", context)


def category_post(request, cats):
    category_post = Post.objects.filter(category=cats.replace("-", " "))
    context = {"cats": cats.title().replace("-", ""), "category_post": category_post}
    return render(request, "blog/category_post.html", context)


class PostPage(DetailView):
    model = Post
    template_name = "blog/post_details.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostPage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        stuff = get_object_or_404(Post, id=self.kwargs["pk"])
        stuffs = get_object_or_404(Post, id=self.kwargs["pk"])

        # total_likes = stuff.total_likes()
        # liked = False
        # if stuff.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        # total_dislikes = stuffs.total_dislikes()
        # disliked = False
        # if stuffs.likes.filter(id=self.request.user.id).exists():
        #     disliked = True

        # context["total_likes"] = total_likes
        # context["liked"] = liked

        # context["total_dislikes"] = total_dislikes
        # context["disliked"] = disliked

        return context


class AddPost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/add_post.html"


class AddCategory(CreateView):
    model = Category
    # form_class = CreatePostForm
    template_name = "blog/add_category.html"
    fields = "__all__"


class CreatePost(View):
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
