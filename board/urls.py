from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('board', views.board_list, name='board_list'),

]