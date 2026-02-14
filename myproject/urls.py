# project_name/urls.py
from django.contrib import admin
from django.urls import path, include, re_path  # Don't forget to import include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token  # Import this here!
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/posts/", include("myApp.urls"), name="post-list"),  # No regex needed!
    path("api-token-auth/", obtain_auth_token),  # <--- Put it here for a clean URL
    # This forwards any request starting with 'welcome/' to your app
    path("welcome/", include("myApp.urls")),
    # This captures 'v1' or 'v2' and passes it to the view
    # re_path(r"^api/(?P<version>(v1|v2))/posts/", include("myApp.urls")),
    # This is your "Login" endpoint to generate tokens
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # This is to get a new access token using a refresh token
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# Add this at the very bottom
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
