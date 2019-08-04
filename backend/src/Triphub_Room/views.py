from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def Room_create(request):
    return render(request,'create.html')

@login_required
def Room_select(request):
    return render(request,'select.html')

@login_required
def Room_loading(request):
    return render(request,'loading.html')
    