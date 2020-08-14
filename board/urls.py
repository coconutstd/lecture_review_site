from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='main'),
    path('board', views.board_list, name='board_list'),
    # board_detail 페이지 작성하기 # localhost:8000/post/5
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
]