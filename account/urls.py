from .views import loginView, accountsView, logout_view
from django.urls import path


urlpatterns = [
    path("", accountsView, name = "accounts"),
    path("login/", loginView, name = "login"),
    path('logout/', logout_view, name='logout'),
]