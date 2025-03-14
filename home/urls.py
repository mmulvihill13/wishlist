from django.urls import path
from. import views
from .views import home

app_name = "home"

urlpatterns = [
    path("", home, name="home"),  # This will be your new home route
    path('account/', views.account_view, name='account'),
]
