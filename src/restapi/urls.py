from django.contrib import admin
from django.urls import path, include

from updates.views import json_example_view, JsonCBV, JsonCBV2, SerializedListView, SerializedDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', include('status.api.urls')),
    path('api/updates/', include('updates.api.urls')),
    # path('', json_example_view),
    # path('json/cbv', JsonCBV.as_view()),
    # path('json/cbv2', JsonCBV2.as_view()),
    # path('json/serialized/list', SerializedListView.as_view()),
    # path('json/serialized/detail', SerializedDetailView.as_view()),
]
