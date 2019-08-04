from django import forms
from .models import RoomInput

class RoomInput(forms.ModelForm):
    class Meta:
        model = RoomInput # 모델을 기반으로
        fields = ['roomname'] # 타이틀과 바디를 입력받을 수 있는 공간을 만들겠다.