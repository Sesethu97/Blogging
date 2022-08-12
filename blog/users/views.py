from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

from .forms import SignupForm, EditProfileForm

# Create your views here.


class UserRegisteration(generic.CreateView):
    form_class = SignupForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:home")


class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("blog:home")

    def get_object(self):
        return self.request.user
