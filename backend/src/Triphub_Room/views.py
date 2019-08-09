from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import RoomInput,myRoom,memberList  # 데이터베이스 틀 임포트
import pymysql.cursors

# django + react api 연동
from rest_framework import viewsets
from .serializers import RoomInputSerializer, myRoomSerializer

@login_required
def ToRoom_create(request):
    return render(request, 'create.html')

@login_required
def Room_create(request):
    room = RoomInput()
    room.roomname = request.GET['roomname'] # 방이름
    room.mainmember = request.user.username # 방장
    room.save() # 쿼리셋 메소드 중 하나. room에 넣은 내용을 저장해라는 함수
    #객체.delete()객체에 해당하는 내용을 데이터베이스 내용을 지워라

    myroom = myRoom()
    myroom.room_id = room.id
    myroom.attraction = ''
    myroom.city = ''
    myroom.name = room.mainmember
    myroom.ispass = '0'
    myroom.save()

    qs = memberList.objects.all()
    rows = qs.filter(user_id__icontains=request.user.username)
    for row in rows:
        originalvalue = row.room_id
        originalvalue += ('&' + str(room.id))
        rows.update(room_id = originalvalue)
        
    # memberList.save()
    # rows.update(room_id += ('&' + room.id))

    return render(request, 'select.html',{'room':myroom})

@login_required
def Room_select(request, room_id):
    room = get_object_or_404(RoomInput, pk = room_id)
    return render(request,'select.html')

@login_required
def Room_loading(request):
    return render(request,'loading.html')

    
    

    