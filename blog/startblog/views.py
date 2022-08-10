from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404, render ,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, EditForm
from startblog.forms import CreatePostForm
from django.urls import reverse_lazy
from .models import Category, Post


class HomePage(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']


class PostPage(DetailView):
    model = Post
    template_name = "post_details.html"


class AddPost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "add_post.html"
 
class AddCategory(CreateView):
    model = Category
    # form_class = CreatePostForm
    template_name = "add_category.html"

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
        return render(request, "add_post.html", {"form": form})


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')
















