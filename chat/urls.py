from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.ShowChatHome, name='ShowChatHome'),
    path('chat/<str:room_name>/<str:person_name>/', views.ShowChatPage, name='ShowChatPage'),

]
