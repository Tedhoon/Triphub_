from django.db import models
from django.contrib.auth.models import User

# 방과 관련된 모델들 -> 방 이름, 방 생성한 날짜, 방장의 이름이 한줄에 들어있음
class RoomInput(models.Model):
    objects = models.Manager()  #빨간줄 안뜨도록하기위해서
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    # 날짜
    roomname = models.CharField(max_length=10)
    # 방이름
    mainmember = models.CharField(max_length=10)
    # 방장

    def __str__(self):
        return self.roomname

# 해당 방마다 관련된 정보 -> 그룹의 도시, 개인이 선택한 여행지, 확인눌렀는지, 
class myRoom(models.Model):
    objects = models.Manager()  #빨간줄 안뜨도록하기위해서

    # 방 id
    room_id = models.CharField(max_length=200)
    # 멤버들 이름
    name = models.CharField(max_length=100)
    # 이 그룹이 여행가는 도시 이름
    city = models.CharField(max_length=100)
    # 개인이 선택한 여행지들
    attractions = models.CharField(max_length=500)
    # 확인 눌렀는지 나타내는 변수
    ispass = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 멤버와 관련된 모델들 -> 회원가입한 사람들의 /아이디, 방아이디가 저장되어있음
class memberList(models.Model):
    objects = models.Manager()  #빨간줄 안뜨도록하기위해서
    user_id = models.CharField(max_length=200)
    # 유저 아이디
    room_id = models.CharField(max_length=200)
    # 방 id

    def __str__(self):
        return self.user_id

# 최종으로 선택된 여행지가 들어있음 -> 방 아이디 -- 여행지 순위, 최종 헌택힌 여행지
class outcome(models.Model):
    objects = models.Manager() 
    #방 이름
    room_id = models.CharField(max_length=200)
    #여행지 순위
    order = models.CharField(max_length=20)
    #최종 선택한 여행지
    attraction = models.CharField(max_length=300)

    def __str__(self):
        return self.room_id

