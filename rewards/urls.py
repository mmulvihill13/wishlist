from django.urls import path
from .views import reward

app_name = "rewards"  

urlpatterns = [
    path('reward/', reward, name='reward'),
]
