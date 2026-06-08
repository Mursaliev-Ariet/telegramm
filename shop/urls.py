from django.urls import path
from .views import (
    FlowerListAPIView,
    FlowerDetailAPIView,
    OfficiantListAPIView,
    OfficiantDetailAPIView,
)

urlpatterns = [
    path("officiants/", OfficiantListAPIView.as_view()),
    path("officiants/<int:pk>/", OfficiantDetailAPIView.as_view()),
    path("flowers/", FlowerListAPIView.as_view()),
    path("flowers/<int:pk>/", FlowerDetailAPIView.as_view()),
]