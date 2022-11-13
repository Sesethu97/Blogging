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
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, EditForm
from startblog.forms import CreatePostForm
from django.urls import reverse_lazy, reverse
from .models import Category, Post, Vote
from typing import Any
from django.http import HttpResponseRedirect
from utils.helpers import check_has_user_voted, cast_vote


class HomePage(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def base_home(request):
    return render(request, 'blog/base_home.html', {})


# def contact_page(request):
#     return render(request, 'blog/contact_page.html', {})

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
        posts_ = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = posts_.total_likes()
        total_dislikes = posts_.total_dislikes()
        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        
        return context




@login_required
def create_post(request: HttpRequest):
    if not request.method == "POST":
        post_form = CreatePostForm()
    else:
        post_form = CreatePostForm(request.POST, request.FILES)


        if not post_form.is_valid():
            messages.error(request, "Post creation failed")
        else:
            post_form = post_form.save(commit=False)
            print(post_form)

            post_form.author = request.user
            post_form.save()
            
            new_post = Post.objects.last()
            return redirect("blog:post_details", pk=new_post.id)
    context = {
        "form": post_form,
    }
    return render(request, "blog/add_post.html", context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_details', args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_details', args=[str(pk)]))

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
