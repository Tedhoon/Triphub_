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
        user_room = user_room[1:]
    qs = RoomInput.objects.all() #유저 정보 모두 가지고 오기

    info = []
    for i in user_room:
        rows = qs.filter(id__icontains=i)
        for row in rows:
            info.append(row)

    return render(request,'main.html', {'infos':info})
