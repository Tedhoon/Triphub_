from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Triphub_Room.models import RoomInput, memberList

@login_required
def main(request):
    
    qs = memberList.objects.all() #유저 정보 모두 가지고 오기
    for row in qs:
        if row.user_id == request.user.username:
            user_room = row.room_id.split('&')
            #유저 방 개수만큼 방을 만듬 -> 유저 방 이름과 함께 띄워주기
            #유저의 방의 개수 배열 user_room
    
    if len(user_room)!= 0:
        user_room = user_room[1:]#방번호 가지고 오기

    qs = RoomInput.objects.all() #유저 정보 모두 가지고 오기
    info = []
    for i in user_room: #방번호로 찾기
        rows = qs.filter(id__icontains=i)
        for row in rows:
            info.append(row)

    userName = request.user.username+'님 안녕하세요'
    return render(request,'main.html', {'infos':info, 'username':userName})

def private_room(request, info_id): 
    room_id = get_object_or_404(RoomInput, pk = info_id)
    room = RoomInput()  #roominput테이블 정보를 대입
    
    qs = RoomInput.objects.all()    #방, 방이름, 방장 정보 가져오기
    row = qs.filter(id__icontains=info_id) #url의 pk값이랑 같은 것을 찾는다

    return render(request,'select.html',{'roomname':row[0].roomname})

