# Triphub_Home.urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]