from django.urls import path
from .views import home

app_name = "home"

urlpatterns = [
    path("", home, name="home"),  # This will be your new home route
]
