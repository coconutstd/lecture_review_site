from django.urls import path
from . import views

urlpatterns = [
    path('timer/', views.TimerHome.as_view() , name="timer_home"),
]
