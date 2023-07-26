from django.views.generic.base import RedirectView
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path("chat/", include('chat.urls'), name = "chat_lobby"),
    path("api-auth/", include('rest_framework.urls')),
    path("inventory/", include('inventory.urls')),
    path("accounts/", include('account.urls')),
    path("", include('dashboard.urls')),
    path("admin/", admin.site.urls),
]
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url = settings.STATIC_URL + 'assets/img/favicon.ico')),
]