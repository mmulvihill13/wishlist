from django.urls import path
from .views import setting, update_user  

app_name = "settings"

urlpatterns = [
    path('', setting, name='setting'),
    path('account/update/', update_user, name='update_user'),  
]
