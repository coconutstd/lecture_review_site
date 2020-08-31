from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='main'),
    path('board', views.board_list, name='board_list'),
    # board_detail 페이지 작성하기 # localhost:8000/post/5
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/new/', views.board_new, name='board_new'),
    path('board/<int:pk>/edit/', views.board_edit, name='board_edit'),
    path('board/<int:pk>/remove/', views.board_remove, name='board_remove'),
    path('board/<int:pk>/comment/', views.add_comment_to_board, name='add_comment_to_board'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
