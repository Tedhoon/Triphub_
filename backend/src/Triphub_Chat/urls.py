# Triphub_Chat.urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.url_room_create, name='url_room_create'),
    path('<room_name>/', views.room, name ="room"),
]