from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("", include(("home.urls", "home"), namespace="home")),  # Set new home app as the default route
    path("login/", include(("login.urls", "login"), namespace="login")),  # Keep login routes
    path('order/', include('order.urls')),
    path('rewards/', include("rewards.urls")),
] + static(settings.STATIC_URL)