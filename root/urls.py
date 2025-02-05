from django.views.generic.base import RedirectView
from django.urls import path, include
from dashboard.views import search
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path("chat/", include('chat.urls'), name = "chat_lobby"),
    path("api-auth/", include('rest_framework.urls')),
    path("inventory/", include('inventory.urls')),
    path("accounts/", include('account.urls')),
    path("search/<search>", search, name="search"),
    path("", include('dashboard.urls')),
    path("UNIQUEINVENTORYADMINISTRATOR174/", admin.site.urls),
]
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url = settings.STATIC_URL + 'assets/img/favicon.ico')),
]