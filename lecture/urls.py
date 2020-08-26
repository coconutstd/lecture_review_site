from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('lecture', views.lecture_list, name='lecture_list'),
    path('book', views.book_list, name='book_list'),
    path('signup', views.signup, name='signup'),
    path('book_type', views.book_type, name='book_type'),
]