# project_name/urls.py
from django.contrib import admin
from django.urls import path, include  # Don't forget to import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # This forwards any request starting with 'welcome/' to your app
    path("welcome/", include("myApp.urls")),
]

# Add this at the very bottom
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
