"""win URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', include('django_admin_filter.urls')),
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('books/', include('books.urls')),
    path('notes/',include('notes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
