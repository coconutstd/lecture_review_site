from django.urls import path
from . import views

urlpatterns = [
    path('review', views.review_list, name='review_list'),
    path('review/<int:question_id>/', views.review_detail, name='review_detail'),
    path('review/<int:question_id>/results/', views.results, name='review_results'),
    path('review/<int:question_id>/vote/', views.vote, name='review_vote'),
]