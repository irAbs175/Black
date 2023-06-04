"""
2020 Black
root URL configuration
developer : #ABS
"""

# Import all requirements
from .local_settings import DEVELOPERS_PANEL, ADMINS_PANEL
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls import handler404, handler500
from wagtail.admin import urls as wagtailadmin_urls
from django.views.generic.base import RedirectView
from product.views import CartView, CheckoutView
from django.urls import include, path, re_path
from django.conf.urls.static import static
from wagtail import urls as wagtail_urls
from django.contrib import admin
from django.conf import settings
from .api import api_router
import os.path


# NOTE : PLEASE KEEP THIS FILE SAFE !
urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('api-auth/', include('rest_framework.urls')),
    path(ADMINS_PANEL, include(wagtailadmin_urls)),
    path('UNIQUEDOC/', include(wagtaildocs_urls)),
    path('cart/', CartView.as_view(), name='cart'),
    path('accounts/', include('allauth.urls')),
    path(DEVELOPERS_PANEL, admin.site.urls),
    path('api/', api_router.urls),

    re_path(r'', include(wagtail_urls)),
]

# Custom static & storage files configuration
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'blog/images/favicon.ico'))
]

# Add the 404-500 error view
handler404 = 'index.views.page_not_found_error'
handler500 = 'index.views.server_error'