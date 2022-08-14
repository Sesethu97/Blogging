from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignupForm, EditProfileForm, PasswordChangedForm

# Create your views here.

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangedForm

    # form_class = PasswordChangeForm
    success_url = reverse_lazy("password_success")

    # success_url = reverse_lazy("blog:home")

def password_success(request):
    return render(request,"registration/password_success.html", {})



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
