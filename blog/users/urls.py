from atexit import register
from re import template
from django.urls import path, include
from .views import UserRegisteration, UserEdit, PasswordChangeView, ShowProfilePageView, EditProfilePage
from django.contrib.auth import views as auth_views
from . import views
app_name = "users"

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path("register/", UserRegisteration.as_view(), name="register"),
    path("edit_profile/", UserEdit.as_view(), name="edit_profile"),
    # path("password/", auth_views.PasswordChangeView.as_view(template_name="registration/change_pwd.html")),
    path("password/", PasswordChangeView.as_view(template_name="registration/change_pwd.html")),
    path("password_success/", views.password_success, name="password_success"),
    path("<int:pk>/profile/", ShowProfilePageView.as_view(), name="show_profile"),
    path("<int:pk>/edit_profile/", EditProfilePage.as_view(), name="edit_profile_info"),

]