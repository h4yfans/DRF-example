from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', include('status.api.urls')),
    path('api/updates/', include('updates.api.urls')),
    path('api/auth/jwt', obtain_jwt_token),
    path('api/auth/jwt/refresh/', refresh_jwt_token),
]
