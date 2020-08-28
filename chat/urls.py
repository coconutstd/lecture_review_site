
from . import views
from django.urls import path
urlpatterns=[
    path('chat/',views.ShowChatHome,name='showchat'),
    path('chat/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]