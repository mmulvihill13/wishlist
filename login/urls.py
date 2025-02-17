from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import authView

app_name = "login"  # This ensures namespacing works correctly

urlpatterns = [
    path("signup/", authView, name="authView"),  # Keeps your signup page
    path("", LoginView.as_view(template_name="registration/login.html"), name="login"),  # Defines a proper login view
    path("accounts/", include("django.contrib.auth.urls")),  # Includes Django's built-in auth URLs
]
