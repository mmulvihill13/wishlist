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
    path('settings/', include("settings.urls")),
    path('cart/', include("cart.urls")),
    path('checkout/', include("checkout.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL)