from atexit import register
from django.urls import path, include
from .views import UserRegisteration


app_name = "users"

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path("register/", UserRegisteration.as_view(), name="register"),
]