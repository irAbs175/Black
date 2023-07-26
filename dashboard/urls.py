from django.urls import path
from .views import index, import_excel


urlpatterns = [
    path("", index, name = "dashboard"),
    path('import_excel', import_excel, name="Import_excel"),
]