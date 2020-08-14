from django.urls import path
from . import views

urlpatterns=[
    path('qna',views.qna_list,name='qna_list'),

]