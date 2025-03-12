from django.urls import path
from .views import account_page, setting

app_name = "settings"  

urlpatterns = [
    path('', setting, name='setting'),
    path('account/', account_page, name='account'),
]
