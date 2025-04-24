from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import authView
from .forms import CustomLoginForm
from django.contrib.auth import views as auth_views

app_name = "login"  # This ensures namespacing works correctly

urlpatterns = [
    path("signup/", authView, name="authView"),  # Keeps your signup page
    path(
        "",
        LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=CustomLoginForm
        ),
        name="login"
    ),
    path("accounts/", include("django.contrib.auth.urls")),  # Includes Django's built-in auth URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
