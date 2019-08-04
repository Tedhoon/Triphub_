from django.db import models
from django.contrib.auth.models import User

# 방과 관련된 모델들
class RoomInput(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    # 날짜
    roomname = models.CharField(max_length=10)
    # 방이름
    mainmember = models.CharField(max_length=10)
    # 방장

    def __str__(self):
        return self.roomname

class myRoom(models.Model):
    room_id = models.CharField(max_length=10)
    # 방 id

    name = models.CharField(max_length=10)
    # 멤버들 이름

    def __str__(self):
        return self.name

# 멤버와 관련된 모델들

class memberList(models.Model):
    user_id = models.CharField(max_length=20)
    # 유저 아이디
    room_id = models.CharField(max_length=10)
    # 방 id

    def __str__(self):
        return self.user_id