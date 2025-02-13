from django.urls import path, include
from .views import authView

urlpatterns = [
    path("signup/",authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),

]
