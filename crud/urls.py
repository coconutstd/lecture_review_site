from django.urls import path
from . import views


urlpatterns = [
    path('crud', views.crud_lecture_list, name='crud_lecture_list'),
    path('crud/<int:lect_id>/', views.eval_list, name = "eval_list"),
    path('crud/<int:lect_id>/write/', views.write, name = "write"),
    path('crud/create/', views.create, name = "create"),
]