from django.urls import path
from .views import (
    StatusAPIView,
    StatusDetailAPIView,
)

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<pk>/', StatusDetailAPIView.as_view()),
]
