# Triphub_Home.urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('room/<int:info_id>/',views.private_room, name='private_room')
]