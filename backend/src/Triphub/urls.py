# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Triphub_Accounts.urls')),
    path('main/',include('Triphub_Home.urls')),
    path('room/',include('Triphub_Room.urls')),
    path('chat/',include('Triphub_Chat.urls')),
    path('place_select/',include('Triphub_Place.urls')),
    
]

