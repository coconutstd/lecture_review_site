from django.shortcuts import render
from django.http import HttpResponse


from .models import nick
from myaccount.models import MyUser

# Create your views here.

def ShowChatHome(request):
    #popo=MyUser.objects.values('nickname')
    #print(popo)

    return render(request,"chat/chat_home.html")


def ShowChatPage(request,room_name,person_name):
    return render(request,"chat/chat_screen.html",{'room_name':room_name,'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)

