# Triphub_Room.urls.py

from django.urls import path
from . import views

# django + react api 연동
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("roominput", views.RoomInputView, "roominput")
# router.register("myroom", views.myRoomView, "myroom")

urlpatterns = [
    path('',views.ToRoom_create, name='ToRoom_create'),
    path('create/',views.Room_create, name='Room_create'),
    path('select/',views.Room_select, name='Room_select'),
    path('loading/', views.Room_loading, name='Room_loading'),

    # 패스를 추가해줬다고 무조건 html을 띄워야 하는 건 아님.
    # path('어떤 url이 들어오면', (어디에있는)어떤 함수를 실행시켜라)
    # 그저 create 함수를 실행시켜주려고 하는 것임.
    
    # django + react api 연동
    # path('api/', include(router.urls)),

]