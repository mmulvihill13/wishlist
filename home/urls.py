from django.urls import path
from . views import home
from . import views

app_name = "home"

urlpatterns = [
    path("", home, name="home"),  # This will be your new home route
    path('reviews/', views.all_reviews, name='all_reviews'),
]
