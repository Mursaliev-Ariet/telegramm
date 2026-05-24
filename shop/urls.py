from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.clothes_list, name='clothes_list'),
]