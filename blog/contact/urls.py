from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include
from .views import contact_views

app_name = "contact_views"

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path('contact/', contact_views, name='contact_views'),
]