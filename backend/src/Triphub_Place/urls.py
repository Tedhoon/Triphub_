# Triphub_Place.urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.place_select , name = "place_select"),
    path('attraction/', views.attraction , name = "attraction" ),
    path('attraction2/', views.attraction2 , name ="attraction2"),
    path('next_select_page/', views.next_select_page, name = "next_select_page"),
]   