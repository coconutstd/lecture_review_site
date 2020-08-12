from django.urls import path
from . import views

urlpatterns = [
    path('review', views.review_list.as_view(), name='review_list'),
    path('review/<int:pk>/', views.review_detail.as_view(), name='review_detail'),
    path('review/<int:question_id>/results/', views.results, name='review_results'),
    path('review/<int:question_id>/vote/', views.vote, name='review_vote'),
]