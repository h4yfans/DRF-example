from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', include('status.api.urls')),
    path('api/updates/', include('updates.api.urls')),
    path('api/auth/', include('accounts.api.urls')),
    path('api/users/', include('accounts.api.user.urls', namespace='api-user')),

]
