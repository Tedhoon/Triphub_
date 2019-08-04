from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/chat/<room_name>/', consumers.ChatConsumer),
]
#여기서도 패스 잘써줘라~!~~!~!~!~!~!~!~!!! 앞에 ws도 꼭!