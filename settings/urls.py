from django.urls import path
from .views import account_page, setting, update_user 
from django.contrib.auth import views as auth_views 
from . import views

app_name = "settings"

urlpatterns = [
    path('', setting, name='setting'),
    path('account/', account_page, name='account'),
    path('account/update/', update_user, name='update_user'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delivery-locations/', views.delivery_locations, name='delivery_locations'),

]
