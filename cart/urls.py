from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
    path('drink-options/<int:drink_id>/', views.get_drink_options, name='get_drink_options')
]
