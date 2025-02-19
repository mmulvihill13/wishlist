from django.urls import path
from .views import menu

app_name = "order"  

urlpatterns = [
    path('menu/', menu, name='menu'),
]
