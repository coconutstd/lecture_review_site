from django.shortcuts import render
from django.http import HttpResponse


from .models import nick
from myaccount.models import MyUser

# Create your views here.

def ShowChatHome(request):
    #popo=MyUser.objects.values('nickname')
    #print(popo)
    user_nickname = nick.objects.filter(id=request.user.get_nickname())[0].nick_nickname
    return render(request,"chat/chat_home.html", {"user_nickname": user_nickname})


def ShowChatPage(request,room_name,person_name):
    return render(request,"chat/chat_screen.html",{'room_name':room_name,'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)

