from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ShowChatHome(request):
    return render(request, "chat/chat_home.html")
    #return HttpResponse('chat page~!~!~!')


def ShowChatPage(request,room_name,person_name):
    #return HttpResponse('chat page '+room_name+""+person_name)
    return render(request,"chat/chat_screen.html",{'room_name':room_name,'person_name':person_name})
