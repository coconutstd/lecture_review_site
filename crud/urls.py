from django.urls import path
from . import views


urlpatterns = [
    path('crud', views.crud_lecture_list, name='crud_lecture_list'),
    path('crud/<int:lect_id>/', views.eval_list, name = "eval_list"),
    path('crud/<int:lect_id>/write/', views.write, name = "write"),
    path('crud/create/', views.create, name = "create"),
    # http://127.0.0.1:8000/eval_detail/3 강의평가한 글마다 key 주기 위함
    path('crud/eval_detail/<int:eval_id>/', views.eval_detail, name="eval_detail"),
    path('crud/<int:eval_id>/update', views.update, name = "update"),
    path('<int:eval_id>/delete', views.delete, name="delete"),
]