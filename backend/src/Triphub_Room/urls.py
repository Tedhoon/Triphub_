# Triphub_Room.urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.Room_create, name='Room_create'),
    path('select/',views.Room_select, name='Room_select'),
    path('loading/', views.Room_loading, name='Room_loading'),
]