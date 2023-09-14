from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('shop/', include('ecommerceapp.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('', include('ecommerceapp.urls')),  # This should be the last pattern
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
