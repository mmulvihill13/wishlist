from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    # path('process/', views.process_order, name='process_order'),
    path('ordered/', views.ordered, name='ordered'),
]
