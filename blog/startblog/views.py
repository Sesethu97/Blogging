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
        context["category_menu"] = category_menu
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



def user_cast_vote(request, pk, vote_value):
    """
    Creates new `Vote` object associated with request.user + `Link.objects.get(object_id=object_id)`
    """
    if not request.user.is_authenticated:
        data = {
            "status_code": 401,
            "message": "You need be logged in to perform this action",
        }
        return HttpResponse(data)
    else:
        post = get_object_or_404(Post, pk=pk)

        try:
            vote_value = int(vote_value)
        except:
            vote_value = 0

        has_user_voted = check_has_user_voted(Vote, request.user, post)

        if has_user_voted == True:
            vote = Vote.objects.get(user=request.user, post=post)
            if vote.value == -1 or vote.value == 1:
                cast_vote(post=post, vote_value=0, vote=vote)
            elif vote.value == 0:
                cast_vote(post=post, vote_value=vote_value, vote=vote)

            return HttpResponse(
                {"score": post.score, "has_voted": True, "value": vote.value}
            )
        elif has_user_voted == False:
            vote = Vote.objects.create(user=request.user, post=post)
            cast_vote(post=post, vote_value=vote_value, vote=vote)
            return HttpResponse({"score": post.score, "has_voted": True})


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
