from django.urls import path
from .views import account_page, setting, update_user  

app_name = "settings"

urlpatterns = [
    path('', setting, name='setting'),
    path('account/', account_page, name='account'),
    path('account/update/', update_user, name='update_user'),  
]
