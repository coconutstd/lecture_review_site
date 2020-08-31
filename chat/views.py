from django.shortcuts import render
from django.http import HttpResponse
from .models import nick

# Create your views here.

def ShowChatHome(request):
    return render(request,"chat/chat_home.html",{'nicks':nick.objects.filter(nick_using=0)})


def ShowChatPage(request,room_name,person_name):
    return render(request,"chat/chat_screen.html",{'room_name':room_name,'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)

