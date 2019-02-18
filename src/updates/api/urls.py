from django.urls import path

from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView
)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('<pk>/', UpdateModelDetailAPIView.as_view()),
]
