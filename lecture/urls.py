from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('lecture', views.lecture_list, name='lecture_list')
]