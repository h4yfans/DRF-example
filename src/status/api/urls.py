from django.urls import path
from .views import (
    StatusAPIView,
    StatusListSearchAPIView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)

urlpatterns = [
    path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<pk>/', StatusDetailAPIView.as_view()),
    # path('<pk>/update', StatusUpdateAPIView.as_view()),
    # path('<pk>/delete', StatusDeleteAPIView.as_view()),
    # path('', json_example_view),
    # path('json/cbv', JsonCBV.as_view()),
    # path('json/cbv2', JsonCBV2.as_view()),
    # path('json/serialized/list', SerializedListView.as_view()),
    # path('json/serialized/detail', SerializedDetailView.as_view()),
]
