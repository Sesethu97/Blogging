from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignupForm, EditProfileForm, PasswordChangedForm
from startblog.models import User


class CreateNewProfileView(CreateView):
    model = User
    template_name = "registerations/create_profile.html"


class EditProfilePage(generic.UpdateView):
    model = User
    template_name = "registration/edit_profile_info.html"
    fields = ["bio", "profile_picture", "website_url", "facebook_url", "twitter_url", "instagram_url", "pinterest_url" ]
    success_url = reverse_lazy("blog:home")



class ShowProfilePageView(DetailView):
    model = User
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangedForm
    success_url = reverse_lazy("users:password_success")


def password_success(request):
    return render(request, "registration/password_success.html", {})


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
