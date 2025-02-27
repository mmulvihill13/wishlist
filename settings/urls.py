from django.urls import path
from .views import setting

app_name = "settings"  

urlpatterns = [
    path('', setting, name='setting'),
]
