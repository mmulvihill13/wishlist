from django.urls import path
from .views import menu
from . import views

app_name = "order"  

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('detailed-menu/<str:drink_name>/', views.detailed_menu, name='detailed_menu'),
]
